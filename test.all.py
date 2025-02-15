import json
import glob
from sinara.step import Step
from sinara.step import StepSafeguard as sg

params = {
    "pipeline_params":
    {
        "env_name":"user",
        "pipeline_name":"pipeline",
        "zone_name":"zone",
    },
    "step_params":
    {
        "Y": "something_else"
    },
    "substeps_params":[ ]
}

try:
    files = glob.glob('test_*.ipynb')
    
    substeps_params = []
    for file in files:
        #print(file)
        substeps_params.append({
            "substep_name": file,
            "substep_params":{}
        })
    
    params["substeps_params"] = substeps_params

    params_filename = "params/test_all_params.json"
    with open(params_filename, 'w') as json_file:
        json.dump(params, json_file, indent=4)
    
    step = Step(step_params_file_globs=params_filename, env_name="user")
    for notebook in step.notebooks:
        notebook.run()
except Exception as e:
    step.handle_exception(e)
finally:
    step.handle_exit()
