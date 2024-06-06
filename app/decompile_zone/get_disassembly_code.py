from app.decompile_zone.function_filter import function_filter
from app.output_functions import output
import subprocess
import shutil
import os

def vrfy_path(path, BINARY_NAME):

    gpr = path + ".gpr"
    rep = path + ".rep"

    if os.path.exists(gpr):
        shutil.rmtree(rep)
        os.remove(gpr)
        output("info", 1, f"Existing project '{BINARY_NAME}' has been removed.")

def get_disassembly_code(BINARY_NAME, TARGET_FILE_PATH, DISASSEMBLY_CODE_PATH, VERBOSE):

    output("+", 0, "Decompiling Binary.")

    ghidra_headless = "/usr/local/bin/ghidra_10.4_PUBLIC/support/analyzeHeadless"
    project_path = "app/decompile_zone/projects"
    script_path = "app/decompile_zone/script"
    post_script = "decompiler.py"
    project_name = BINARY_NAME

    ghidra_cmd = [
        ghidra_headless,
        project_path,
        project_name,
        "-import", TARGET_FILE_PATH,
        "-scriptPath", script_path,
        "-postScript", post_script, DISASSEMBLY_CODE_PATH
    ]

    vrfy_path(f"{project_path}/{project_name}", BINARY_NAME)

    try:
        result = subprocess.run(ghidra_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            output("+", 1, 'Pseudocode generation completed successfully.')
        else:
            output("-", 1, f'Pseudocode generation failed: {result.stderr}')
    except Exception as e:
        output("-", 1, f'An error occurred while running Ghidra headless: {e}')

    functions = function_filter(DISASSEMBLY_CODE_PATH)
    
    return functions