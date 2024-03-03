import sys
import subprocess

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

# --- COMMAND ---
FILE_CMD = ['file', '-b', FILENAME]
CHECKSEC_CMD = ['checksec', '--output=json', '--file=' + FILENAME]

def filter_file_output(output):
    output_list = output.split(', ')
    file_cmd_info = [
        ((output_list[0]).split(' '))[0],
        ((output_list[0]).split(' '))[1],
        output_list[3],
        output_list[7]
    ]
    print(file_cmd_info)

def main():
    file_cmd_output = subprocess.check_output(FILE_CMD, universal_newlines=True)
    filter_file_output(file_cmd_output)

    checksec_cmd_output = subprocess.check_output(CHECKSEC_CMD, universal_newlines=True)
    print(checksec_cmd_output)
main()