import subprocess
from app.output_functions import output

def fuzztest(binary_info: dict, path: str, VERBOSE: bool) -> dict:
    '''
        to test all string from the binary in input.
    '''
    output('+', 0, 'Fuzz testing level 0:')
    wordlist = binary_info['printed strings']

    level_0 = {
        'success':[], 
        'error':[]
    }

    for string in wordlist:

        fuzz_cmd = f'echo "{string}" | ./{path}'
        result = subprocess.run(fuzz_cmd, shell=True, text=True, capture_output=True, check=False)
        success = result.stdout
        error = result.stderr

        if success:
            output('+', 1, f'Successfull with input: {string}')
            level_0['success'].append(string)
        elif error and VERBOSE:
            output('-', 1, f'Error with input: {string}')
            level_0['error'].append(string)

    return level_0