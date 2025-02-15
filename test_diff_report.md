# How to run test diff report
1. Clone this repo inside sinara-notebook:latest container
2. Go to sinara_quick_test folder
3. Ensure that **dev** branch in sinara_quick_test exists

    ```
    git checkout dev
    git checkout main
    ```
    
4. Execute command in jupyter terminal

    ```
    python test_diff_report.py
    ```

## Successful test run example

Diff report creating:

        CURRENT BRANCH: dev
        CURRENT COMMIT: dc1037ab4a990adbce1d52eceb8dadffc98d07c3
        CURRENT RUN: run-23-11-19-075525
        CURRENT RUN PATH: /data/home/jovyan/pipeline/zone/sinara_quick_test/run-23-11-19-075525

        TARGET BRANCH: main
        TARGET COMMIT: c42656b56911b5c805ffc7fd6cee4540a7b8f519
        TARGET RUN: run-23-11-17-135458
        TARGET RUN PATH: /data/home/jovyan/pipeline/zone/sinara_quick_test/run-23-11-17-135458

        Preparing tmp diff report inside of '/home/jovyan/work/sinara_quick_test/tmp/diff.run-23-11-19-075525.run-23-11-17-135458':
        Copying tmp diff report to 'hdfs:///data/home/jovyan/pipeline/zone/sinara_quick_test/run-23-11-19-075525/diff.run-23-11-19-075525.run-23-11-17-135458'
        Tagging current commit by DIFF TAG...
        DIFF TAG: diff.run-23-11-19-075525.run-23-11-17-135458
        Diff report created

## Known-issues.

In case of 
stderr: 'fatal: tag 'diff.run-23-11-19-075525.run-23-11-17-135458' already exists'

please, issue:

```
git tag -d diff.run-23-11-19-075525.run-23-11-17-135458
git push --delete origin diff.run-23-11-19-075525.run-23-11-17-135458
```

In case of

        Preparing tmp diff report inside of '/home/jovyan/work/sinara_quick_test/tmp/diff.run-23-11-19-075525.run-23-11-17-135458':
local diff report wasn't created due to it already exists

```
rm -rf /home/jovyan/work/sinara_quick_test/tmp/diff.run-23-11-19-075525.run-23-11-17-135458
```