from sinara.step import Step
from sinara.step import StepSafeguard as sg
from sinara.step import StepReport as sr

sg.step_is_in_dir("**/work/**")
sg.step_is_in_branch(["main","ver*"])
sg.git_reset()

try:
    step = Step(step_params_file_globs="params/test_step_params.json",
           env_name="user")
    for notebook in step.notebooks:
        notebook.run()
except Exception as e:
    step.handle_exception(e)
finally:
    sr.save()
    sr.tag_commit_by_run()
    step.handle_exit()
