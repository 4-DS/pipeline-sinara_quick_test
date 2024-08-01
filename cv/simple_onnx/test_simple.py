# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
import tempfile
from unittest import TestCase

import torch
from torch import nn
import torch.utils.model_zoo as model_zoo
import torch.onnx
import torch.nn.init as init
import onnx
import onnxruntime
from parameterized import parameterized
import numpy as np

# https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html
class SuperResolutionNet(nn.Module):
    def __init__(self, upscale_factor, inplace=False):
        super(SuperResolutionNet, self).__init__()

        self.relu = nn.ReLU(inplace=inplace)
        self.conv1 = nn.Conv2d(1, 64, (5, 5), (1, 1), (2, 2))
        self.conv2 = nn.Conv2d(64, 64, (3, 3), (1, 1), (1, 1))
        self.conv3 = nn.Conv2d(64, 32, (3, 3), (1, 1), (1, 1))
        self.conv4 = nn.Conv2d(32, upscale_factor ** 2, (3, 3), (1, 1), (1, 1))
        self.pixel_shuffle = nn.PixelShuffle(upscale_factor)

        self._initialize_weights()

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv3(x))
        x = self.pixel_shuffle(self.conv4(x))
        return x

    def _initialize_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight)

class TestSimpleOnnx(TestCase):
    def setUp(self):
        self.torch_model = SuperResolutionNet(upscale_factor=3)

        # Load pretrained model weights
        # model_url = 'https://s3.amazonaws.com/pytorch/test_data/export/superres_epoch100-44c6958e.pth'
        # model = model_zoo.load_url(model_url, map_location=map_location)

        model = torch.load('tests/data/superres_epoch100-44c6958e.pth')
        self.batch_size = 1    # just a random number

        # Initialize model with the pretrained weights
        map_location = lambda storage, loc: storage
        if torch.cuda.is_available():
            map_location = None
        self.torch_model.load_state_dict(model)

        # set the model to inference mode
        self.torch_model.eval()

        # Input to the model
        self.x = torch.randn(self.batch_size, 1, 224, 224, requires_grad=True)
        self.torch_out = self.torch_model(self.x)

    def test_export(self):
        # Export the model
        torch.onnx.export(self.torch_model,               # model being run
                        self.x,                         # model input (or a tuple for multiple inputs)
                        "super_resolution.onnx",   # where to save the model (can be a file or file-like object)
                        export_params=True,        # store the trained parameter weights inside the model file
                        opset_version=10,          # the ONNX version to export the model to
                        do_constant_folding=True,  # whether to execute constant folding for optimization
                        input_names = ['input'],   # the model's input names
                        output_names = ['output'], # the model's output names
                        dynamic_axes={'input' : {0 : 'batch_size'},    # variable length axes
                                        'output' : {0 : 'batch_size'}})
    
    def text_onnx(self):
        onnx_model = onnx.load("super_resolution.onnx")
        onnx.checker.check_model(onnx_model)
    
    @parameterized.expand([
        'CPUExecutionProvider', 'CUDAExecutionProvider',
    ])
    def test_onnxruntime(self, provider):
        ort_session = onnxruntime.InferenceSession("super_resolution.onnx", providers=[provider])

        ort_session_provider = ort_session.get_provider_options()
        
        assert ort_session_provider.get(provider) is not None, f"{provider=} not match in {list(ort_session_provider)}"

        def to_numpy(tensor):
            return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()

        # compute ONNX Runtime output prediction
        ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(self.x)}
        ort_outs = ort_session.run(None, ort_inputs)

        # compare ONNX Runtime and PyTorch results
        np.testing.assert_allclose(to_numpy(self.torch_out), ort_outs[0], rtol=1e-03, atol=1e-05)
