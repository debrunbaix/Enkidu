import sys

from analyse import filter_file_output, filter_checksec_output, filter_strings_output

FILENAME = sys.argv[1]
BINARY_NAME = (FILENAME.split('/'))[-1]

def main():
    obj_binary_info = filter_file_output(FILENAME)

    obj_binary_info.update(filter_checksec_output(FILENAME))

    obj_binary_info.update(filter_strings_output(FILENAME))

    print(obj_binary_info)

main()