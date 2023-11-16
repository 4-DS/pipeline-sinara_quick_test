#!/bin/bash

rm -rf /home/jovyan/work/mmdetection
ln -s /home/jovyan/mmdetection /home/jovyan/work/mmdetection

cd /home/jovyan/work/mmdetection
python demo/image_demo.py demo/demo.jpg rtmdet-s
python demo/image_demo.py demo/demo.jpg rtmdet-ins-s --show