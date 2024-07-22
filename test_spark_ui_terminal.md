# Description
This test ensures that Sinara correctly prints Spark UI url when running interactively and from job in terminal

# How to run sinara archive perfomance test
```
git clone --recursive https://github.com/4-DS/pipeline-sinara_quick_test
cd pipeline-sinara_quick_test
```

Job run test:
```
python test_spark_ui_terminal.py
```

Terminal run test:
1. Open test_spark_ui_terminal.ipynb
2. Run notebook, check Spark UI is accessible using server's IP