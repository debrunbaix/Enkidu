import subprocess
import json

from app.output_functions import output
#
# List of vulnerable functions
#
VULN_FUNCTIONS = [
    'gets',
    'strcpy',
    'strcat',
    'sprintf',
    'scanf',
    'printf',
    'vsprintf',
    'makepath',
    '_splitpath',
    'sscanf',
    'snscanf',
    'strlen'
]

#
# List of string to detect important printed string
#
PRINTED_STRING_LIST = [
    'pass', 'log', 'error', 'user', 'admin', 'name', 'credential', 'input', 'Enter', 'failed',
    'password', 'auth', 'authenticate', 'authentication',
    'login', 'logout', 'connect', 'disconnect',
    'warning', 'invalid', 'unauthorized',
    'username', 'user_id', 'user_name',
    'input_data', 'input_field', 'enter',
    'administrator', 'admin_id', 'authorization', 'permission',
    'credentials', 'identity', 'ID',
    'prompt', 'confirm', 'proceed', 'continue', 'success'
]

#
# function to put the command 'file' informations on an object
#
def file_cmd(FILENAME: str, VERBOSE: bool) -> dict:
    """
        format argument for file command and run it. 
        return the result in object format
    """
    FILE_CMD = ['file', '-b', FILENAME]
    file_cmd_output = subprocess.check_output(FILE_CMD, universal_newlines=True)

    if VERBOSE:
        output('info', 1, file_cmd_output)

    output_list = file_cmd_output.split(', ')
    file_cmd_info = {
        "format": ((output_list[0]).split(' '))[0],
        "bit": 32 if ((output_list[0]).split(' '))[1] == "32-bit" else 64,
        "linked": output_list[3],
        "stripped": "no" if "not" in output_list[7] else "yes"
    }
    return file_cmd_info

#
# function to put the checksec command output in an object
#
def checksec_cmd(FILENAME: str, VERBOSE: bool) -> dict:
    """
        format argument for checksec command and run it. 
        return the result in object format
    """
    CHECKSEC_CMD = ['/usr/bin/checksec', '--output=json', '--file=' + FILENAME]
    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)

    if VERBOSE:
        output('info', 1, checksec_cmd_output)

    output_list = json.loads(checksec_cmd_output)[FILENAME]
    return output_list

#
# Function to analyse the strings command output and store it in object to get :
#   - Vulnerable function
#   - printed strings
#
def strings_cmd(FILENAME: str, VERBOSE: bool) -> dict:
    """
        format argument for strings command and run it. 
        return the result in object format
    """

    STRINGS_CMD = ['strings', FILENAME]

    # try:
    #     strings_cmd_output = subprocess.check_output(STRINGS_CMD, universal_newlines=True)
    # except:
    #     print(f'error doing \'{"".join(STRINGS_CMD)}\' command')
    #     return {
    #     'printed strings': "error",
    #     'vulnerable_functions': "error"
    # }
    strings_cmd_output = subprocess.check_output(STRINGS_CMD, universal_newlines=True)

    printed_string = []
    vulnerable_functions = []

    for function in VULN_FUNCTIONS:
        if function in strings_cmd_output:
            vulnerable_functions.append(function)

    for string in strings_cmd_output.splitlines():
        if VERBOSE:
            output('info', 1, string)
        for word in PRINTED_STRING_LIST:
            if word.lower() in string.lower() and string not in printed_string:
                printed_string.append(string)

    return {
        'printed strings': printed_string,
        'vulnerable_functions': vulnerable_functions
    }

#
# Function to get library list of the binary
#
def ldd_cmd(FILENAME: str, VERBOSE: bool) -> dict:
    """
        format argument for ldd command and run it. 
        return the result in object format
    """
    LDD_CMD = ['ldd', FILENAME]
    ldd_cmd_output = subprocess.check_output(LDD_CMD, universal_newlines=True)

    if VERBOSE:
        output('info', 1, ldd_cmd_output)

    library = []

    for lib in ldd_cmd_output.splitlines():
        library.append(((lib.strip()).split(' '))[0])

    return {
        'library': library
    }
