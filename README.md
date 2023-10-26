# How to run anomalib test
1. Clone this repo inside sinara-cv:latest container
2. Go to sinara_quick_test/anomalib folder
3. Execute command in jupyter terminal

    ```
    bash test_anomalib.sh
    ```
# How to run mmcv + mmdetection test
1. Clone this repo inside sinara-cv:latest container
2. Go to sinara_quick_test/mmcv folder
3. Execute command in jupyter terminal

    ```
    prepare_mmcv_mmdet.sh
    ```
    Environment will be prepared to run tests
4. Go to /home/jovyan/work/mmdetection/demo folder<br>
6. Run notebook

# How to run pytorch lightning test
1. Clone this repo inside sinara-cv:latest container
2. Go to sinara_quick_test folder
3. Execute command in jupyter terminal

    ```
    python pytorch_lightning_test.py
    ```