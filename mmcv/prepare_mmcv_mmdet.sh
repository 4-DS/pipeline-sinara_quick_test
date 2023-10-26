#!/bin/bash

current_dir=$(pwd)
set -e
rm -rf /home/jovyan/work/mmdetection
ln -s /home/jovyan/mmdetection /home/jovyan/work/mmdetection
mkdir -p /home/jovyan/mmdetection/checkpoints
cd /home/jovyan/mmdetection/checkpoints
rm -rf faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
wget https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
\cp -r "${current_dir}/inference_demo.ipynb" /home/jovyan/mmdetection/demo/inference_demo.ipynb
echo "Preparation done. Now you can run demo examples from mmdetection/demo subfolder\n"
echo "Make sure to change relative paths to absolute in inference example notebook"