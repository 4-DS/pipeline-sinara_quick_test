#!/bin/bash -e

# Install libs
pip3 install parameterized pytest

# Test all base
python3 -m pytest simple_onnx
python3 config_mmdet.py
python3 -m pytest mmdet_tests
python3 -m pytest mmdeploy_tests
python3 -m pytest onnxruntime_tests/*

# FOR EXP ONLY

python -m pytest mmsegmentation_tests
python -m pytest mmocr_tests
python -m pytest mmpose_test