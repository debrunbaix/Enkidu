import sys
import subprocess
import json

VULN_FUNCTIONS = [
    'gets',
    'strcpy',
    'strcat',
    'sprintf',
    'scanf',
    'printf'
]

def filter_file_output(FILENAME):

    FILE_CMD = ['file', '-b', FILENAME]
    file_cmd_output = subprocess.check_output(FILE_CMD, universal_newlines=True)

    output_list = file_cmd_output.split(', ')
    file_cmd_info = {
        "format": ((output_list[0]).split(' '))[0],
        "bit": 32 if ((output_list[0]).split(' '))[1] == "32-bit" else 64,
        "linked": output_list[3],
        "stripped": "no" if "not" in output_list[7] else "yes"
    }
    return file_cmd_info

def filter_checksec_output(FILENAME):

    CHECKSEC_CMD = ['checksec', '--output=json', '--file=' + FILENAME]
    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)

    output_list = json.loads(checksec_cmd_output)[FILENAME]
    return output_list

def filter_strings_output(FILENAME):

    STRINGS_CMD = ['strings', FILENAME]
    strings_cmd_output = subprocess.check_output(STRINGS_CMD, universal_newlines=True)

    vulnerable_functions = []

    for function in VULN_FUNCTIONS:
        if function in strings_cmd_output:
            vulnerable_functions.append(function)

    return {
        'vulnerable_functions': vulnerable_functions
    }

def analyse(FILENAME):
    obj_binary_info = filter_file_output(FILENAME)

    obj_binary_info.update(filter_checksec_output(FILENAME))

    obj_binary_info.update(filter_strings_output(FILENAME))

    print(obj_binary_info)
