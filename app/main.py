import sys
import json
from output_functions import output
from enumerate import file_cmd, checksec_cmd, strings_cmd, ldd_cmd
from get_src_code import get_src_code

def run_command(cmd_func, file_path, desc, binary_info):
    try:
        binary_info.update(cmd_func(file_path))
        output('+', 1, f'Information de \'{desc}\' ajoutées.')
    except Exception as e:
        output('-', 1, f'Erreur lors de la commande \'{desc}\': {e}')

def main():
    #
    # get target file path and name
    #
    TARGET_FILE_PATH = sys.argv[1]
    BINARY_NAME = (TARGET_FILE_PATH.split('/'))[-1]

    binary_info = {"name": BINARY_NAME}

    try:
        binary = open(TARGET_FILE_PATH, 'rb')
        output('+', 0, f'Success opening {BINARY_NAME}.')
    except:
        output('-', 0, 'File doesn\'t exist.')
        return 0
    
    #
    # extract information from the binary
    #
    output('+', 0, 'Extracting informations')
    run_command(file_cmd, TARGET_FILE_PATH, 'file', binary_info)
    run_command(checksec_cmd, TARGET_FILE_PATH, 'checksec', binary_info)
    run_command(strings_cmd, TARGET_FILE_PATH, 'strings', binary_info)
    run_command(ldd_cmd, TARGET_FILE_PATH, 'ldd', binary_info)

    # print(json.dumps(binary_info, indent=4))

    #
    # Get source code of the binary
    #
    get_src_code(binary_info, binary)

    return 1

if __name__ == "__main__":
    main()