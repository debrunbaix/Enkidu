import sys
import json

from enumerate import file_cmd, checksec_cmd, strings_cmd, ldd_cmd
from get_src_code import get_src_code

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

binary_info = {"name": BINARY_NAME}

def main():
    try:
        binary = open(FILENAME, 'rb')
    except:
        print('File doesn\'t exist.\n')
        return 0
    
    #
    # extract information from the binary
    #

    binary_info.update(file_cmd(FILENAME))

    binary_info.update(checksec_cmd(FILENAME))

    binary_info.update(strings_cmd(FILENAME))

    binary_info.update(ldd_cmd(FILENAME))

    print(json.dumps(binary_info, indent=4))


    #
    # Get source code of the binary
    #

    get_src_code(binary_info, binary)

    return 1

main()