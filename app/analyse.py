import sys
import subprocess
import json

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

# --- COMMAND ---
FILE_CMD = ['file', '-b', FILENAME]
CHECKSEC_CMD = ['checksec', '--output=json', '--file=' + FILENAME]

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

def main():
    file_cmd_output = subprocess.check_output(FILE_CMD, universal_newlines=True)
    obj_binary_info = filter_file_output(file_cmd_output)

    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)
    obj_binary_info.update(filter_checksec_output(checksec_cmd_output))

    for x in obj_binary_info:
        print(f'{x} : {obj_binary_info[x]}')
main()