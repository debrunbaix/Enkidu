#
# External library
#
import datetime
import argparse
import time
import os

#
# Enkidu modules
#
from app.enumeration.enum import launch_enum_cmd
from app.analyse.analyse import analyse
from app.output_functions import output, TITLE
from app.report import generate_report
from app.fuzztesting import fuzztest

#
# Args management
#
parser = argparse.ArgumentParser(description='Target File')
parser.add_argument(
    '-t', '--target',
    type=str, required=True, 
    help='Mettre un binaire en input'
)
parser.add_argument(
    '-v', '--verbose', 
    action='store_true', required=False, 
    help='Affiche plus d\'informations sur l\'execution en cours'
)
parser.add_argument(
    '-f', '--fuzzlevel',
    type=int, required=True,
    help='Choisir le niveau de fuzztesting à faire :\n - 0 : Seulement tester les strings trouvé dans le binaire\n - 1 : Utilisation de AFL pour le fuzztesting.'
)
args = parser.parse_args()

#
# Const declaration
#
VERBOSE = args.verbose
FUZZLEVEL = args.fuzzlevel
TARGET_FILE_PATH = args.target
BINARY_NAME = (TARGET_FILE_PATH.split('/'))[-1]
TODAY_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
REPORT_FOLDER_OUPUT = f"{BINARY_NAME}_report_{TODAY_DATE}"

def main():
    print(TITLE)
    time.sleep(1)

    binary_info = {"name": BINARY_NAME}

    try:
        binary = open(TARGET_FILE_PATH, 'rb')
        output('+', 0, f'Success opening {BINARY_NAME}.')
    except:
        output('-', 0, 'File doesn\'t exist.')
        exit()
    
    if not os.path.exists(REPORT_FOLDER_OUPUT):
        os.makedirs(REPORT_FOLDER_OUPUT)

    # ENUMERATION PHASE
    launch_enum_cmd(TARGET_FILE_PATH, binary_info, VERBOSE)

    # ANALYSIS PHASE
    assembly_code, rodata_sections = analyse(binary_info, binary, VERBOSE)

    # EXPLOIT ANALYSIS
    fuzz_output_0, fuzz_output_1 = fuzztest(binary_info, TARGET_FILE_PATH, VERBOSE, FUZZLEVEL)

    # REPORT GENERATOR ANALYSIS
    generate_report(
        binary_info, 
        TARGET_FILE_PATH, 
        REPORT_FOLDER_OUPUT, 
        assembly_code,
        fuzz_output_0
    )
    return 1

if __name__ == "__main__":
    main()