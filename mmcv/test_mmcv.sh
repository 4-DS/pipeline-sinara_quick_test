#!/bin/bash

cd /home/jovyan/work/mmdetection
python demo/image_demo.py demo/demo.jpg rtmdet-s
python demo/image_demo.py demo/demo.jpg rtmdet-ins-s