#
# External library
#
import datetime
import argparse
import time
import sys
import os

#
# Enkidu modules
#
from app.decompile_zone.get_disassembly_code import get_disassembly_code
from app.ai_assist.ai_analyse import pseudoc_to_readablec
from app.exploit_test.exploit_test import exploit_test
from app.enumeration.enum import launch_enum_cmd
from app.output_functions import output, TITLE
from app.analyse.analyse import analyse
from app.report import generate_report
from app.fuzztesting import fuzztest

#
# Args management
#
parser = argparse.ArgumentParser(description='Target File')
parser.add_argument(
    '-t', '--target',
    type=str, required=True, 
    help='Mettre un binaire en input.'
)
parser.add_argument(
    '-v', '--verbose', 
    action='store_true', required=False, 
    help='Affiche plus d\'informations sur l\'execution en cours.'
)
parser.add_argument(
    '-ai', '--aiAssist',
    action='store_true', required=False,
    help='Permet d\'améliorer la compréhension des résultats grâce à l\'API de ChatGPT.'
)
args = parser.parse_args()

#
# Const declaration
#
VERBOSE = args.verbose
AI_ASSIST = args.aiAssist
TARGET_FILE_PATH = args.target
BINARY_NAME = (TARGET_FILE_PATH.split('/'))[-1]
TODAY_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
REPORT_FOLDER_OUPUT = f"{BINARY_NAME}_report_{TODAY_DATE}"
DISASSEMBLY_CODE_PATH = f"{REPORT_FOLDER_OUPUT}/disassembly_code"

def main() -> int:
    '''
        main function
    '''
    print(TITLE)
    time.sleep(1)

    binary_info = {"name": BINARY_NAME}

    try:
        binary = open(TARGET_FILE_PATH, 'rb')
        output('+', 0, f'Successfully opened {BINARY_NAME} binary.')
    except FileNotFoundError:
        output('-', 0, 'File doesn\'t exist.')
        sys.exit()

    if not os.path.exists(REPORT_FOLDER_OUPUT):
        os.makedirs(REPORT_FOLDER_OUPUT)
        os.makedirs(DISASSEMBLY_CODE_PATH)

    # ENUMERATION PHASE
    launch_enum_cmd(TARGET_FILE_PATH, binary_info, VERBOSE)

    # GETTING SOURCE CODE
    assembly_code = analyse(binary_info, binary, VERBOSE)
    disassembly_function = get_disassembly_code(BINARY_NAME, TARGET_FILE_PATH, DISASSEMBLY_CODE_PATH, VERBOSE)

    # EXPLOITING/TESTING
    fuzz_output_0 = fuzztest(binary_info, TARGET_FILE_PATH, VERBOSE)
    exploit_object = exploit_test(binary_info, TARGET_FILE_PATH, VERBOSE)

    # AI ASSIST
    if AI_ASSIST :
        disassembly_function = pseudoc_to_readablec(disassembly_function, DISASSEMBLY_CODE_PATH, VERBOSE)

    # REPORT GENERATOR
    generate_report(
        binary_info,
        TARGET_FILE_PATH,
        REPORT_FOLDER_OUPUT,
        assembly_code,
        fuzz_output_0,
        disassembly_function,
        DISASSEMBLY_CODE_PATH,
        exploit_object
    )
    return 1

if __name__ == "__main__":
    main()
