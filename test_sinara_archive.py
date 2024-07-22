from sinara.step import Step

try:
    step = Step(step_params_file_globs="params/test_sinara_archive_params.json",
           env_name="user")
    for notebook in step.notebooks:
        notebook.run()
except Exception as e:
    step.handle_exception(e)
finally:
    step.handle_exit()