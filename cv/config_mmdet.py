# fix for local testing, without git clone
# https://github.com/open-mmlab/mmdetection/blob/main/mmdet/testing/_utils.py#L17

import mmdet
import os
import os.path as osp
from pathlib import Path

if __name__ == "__main__":
    mmdet_config_dir = osp.join(osp.dirname(mmdet.__file__), ".mim", "configs")
    mmdet_config_dir_without_mim = osp.join(osp.dirname(mmdet.__file__), "..", "configs")
    # !ln -s {mmdet_config_dir} {mmdet_config_dir_without_mim}
    if os.path.exists(mmdet_config_dir_without_mim):
        os.remove(mmdet_config_dir_without_mim)
    Path(mmdet_config_dir_without_mim).symlink_to(mmdet_config_dir)

    mmdet_model_index = osp.join(osp.dirname(mmdet.__file__), ".mim", "model-index.yml")
    mmdet_model_index_without_mim = osp.join(osp.dirname(mmdet.__file__), "..", "model-index.yml")
    # !ln -s {mmdet_model_index} {mmdet_model_index_without_mim}
    if os.path.exists(mmdet_model_index_without_mim):
        os.remove(mmdet_model_index_without_mim)
    Path(mmdet_model_index_without_mim).symlink_to(mmdet_model_index)