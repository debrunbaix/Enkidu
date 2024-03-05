import sys
import subprocess
import json

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

# --- COMMAND ---
FILE_CMD = ['file', '-b', FILENAME]
CHECKSEC_CMD = ['checksec', '--output=json', '--file=' + FILENAME]
STRINGS_CMD = ['strings', FILENAME]

VULN_FUNCTIONS = [
    'gets',
    'strcpy',
    'strcat',
    'sprintf',
    'scanf',
    'printf'
]

def filter_file_output(output):
    output_list = output.split(', ')
    file_cmd_info = {
        "format": ((output_list[0]).split(' '))[0],
        "bit": 32 if ((output_list[0]).split(' '))[1] == "32-bit" else 64,
        "linked": output_list[3],
        "stripped": "no" if "not" in output_list[7] else "yes"
    }
    return file_cmd_info

def filter_checksec_output(output):
    output_list = json.loads(output)[FILENAME]
    return output_list

def filter_strings_output(output):

    vulnerable_functions = []

    for function in VULN_FUNCTIONS:
        if function in output:
            vulnerable_functions.append(function)

    return {
        'vulnerable_functions': vulnerable_functions
    }

def main():
    file_cmd_output = subprocess.check_output(FILE_CMD, universal_newlines=True)
    obj_binary_info = filter_file_output(file_cmd_output)

    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)
    obj_binary_info.update(filter_checksec_output(checksec_cmd_output))

    strings_cmd_output = subprocess.check_output(STRINGS_CMD, universal_newlines=True)
    obj_binary_info.update(filter_strings_output(strings_cmd_output))

    print(obj_binary_info)

main()