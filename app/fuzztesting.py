import subprocess
from app.output_functions import output

def fuzztest(binary_info, path, VERBOSE):

    output('+', 0, 'Fuzzing level 1.')
    wordlist = binary_info['printed strings']

    for string in wordlist:
        
        FUZZ_CMD = f'echo "{string}" | ./{path}'
        result = subprocess.run(FUZZ_CMD, shell=True, text=True, capture_output=True)
        success = result.stdout
        error = result.stderr

        if success:
            output('+', 1, f'Success with : {string}')
        elif error and VERBOSE:
            output('-', 1, f'Error with : {string}')