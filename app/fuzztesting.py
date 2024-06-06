import subprocess
from app.output_functions import output

def fuzztest(binary_info, path, VERBOSE):

    output('+', 0, 'Fuzzing level 0.')
    wordlist = binary_info['printed strings']

    level_0 = {
        'success':[], 
        'error':[]
    }

    for string in wordlist:

        FUZZ_CMD = f'echo "{string}" | ./{path}'
        result = subprocess.run(FUZZ_CMD, shell=True, text=True, capture_output=True)
        success = result.stdout
        error = result.stderr

        if success:
            output('+', 1, f'Success with : {string}')
            level_0['success'].append(string)
        elif error and VERBOSE:
            output('-', 1, f'Error with : {string}')
            level_0['error'].append(string)

    return level_0