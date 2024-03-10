import sys
import json

from enumerate import file_cmd, checksec_cmd, strings_cmd, ldd_cmd

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

obj_binary_info = {"name": BINARY_NAME}

def main():

    # extract information from the binary

    obj_binary_info.update(file_cmd(FILENAME))

    obj_binary_info.update(checksec_cmd(FILENAME))

    obj_binary_info.update(strings_cmd(FILENAME))

    obj_binary_info.update(ldd_cmd(FILENAME))

    print(json.dumps(obj_binary_info, indent=4))

main()