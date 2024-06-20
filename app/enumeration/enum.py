from .enum_cmd import file_cmd, checksec_cmd, strings_cmd, ldd_cmd
from ..output_functions import output

#
# Loop to run command with error management
#
def run_command(cmd_func, file_path, desc, binary_info, VERBOSE):
    try:
        binary_info.update(cmd_func(file_path, VERBOSE))
        output('+', 1, f'Added \'{desc}\' informations.')
    except Exception as e:
        output('-', 1, f'Erreur lors de la commande \'{desc}\': {e}')

#
# Extract information from the binary
#
def launch_enum_cmd(TARGET_FILE_PATH, binary_info, VERBOSE):

    output('+', 0, 'Extracting informations:')

    run_command(file_cmd, TARGET_FILE_PATH, 'file', binary_info, VERBOSE)
    run_command(checksec_cmd, TARGET_FILE_PATH, 'checksec', binary_info, VERBOSE)
    run_command(strings_cmd, TARGET_FILE_PATH, 'strings', binary_info, VERBOSE)
    run_command(ldd_cmd, TARGET_FILE_PATH, 'ldd', binary_info, VERBOSE)

    # print(json.dumps(binary_info, indent=4))