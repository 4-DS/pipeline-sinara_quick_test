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
    bash test_mmcv.sh
    ```
4. Results will be palced to /home/jovyan/work/mmdetection/output folder

# How to run pytorch lightning test
1. Clone this repo inside sinara-cv:latest container
2. Go to sinara_quick_test folder
3. Execute command in jupyter terminal

    ```
    python pytorch_lightning_test.py
    ```
    
# How to run step test
!!! Be careful, this test will lose all unsaved work !!!
1. Clone this repo inside sinara-notebook:latest container
2. Go to sinara_quick_test folder
3. Run **Init_Data_sinara_quick_test.ipynb**
4. Execute command in jupyter terminal

    ```
    python test_step.py
    ```