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

# How to run test diff report
1. Clone this repo inside sinara-notebook:latest container
2. Go to sinara_quick_test folder
3. Ensure that **dev** branch in sinara_quick_test exists
4. Execute command in jupyter terminal

    ```
    python test_diff_report.py
    ```

5. In case of 
stderr: 'fatal: tag 'diff.run-23-11-19-075525.run-23-11-17-135458' already exists'

please, issue:

```
git tag -d diff.run-23-11-19-075525.run-23-11-17-135458
git push --delete origin diff.run-23-11-19-075525.run-23-11-17-135458
```