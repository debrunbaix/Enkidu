from capstone import *

from app.output_functions import output

def save_assembly_to_file(assembly_instructions: list, filename: str):
    """
        put assembly in file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        for instruction in assembly_instructions:
            file.write(instruction + "\n")

def get_assembly_code(elffile, mode: str, VERBOSE: bool) -> list:
    """
        get assembly code
    """
    code = elffile.get_section_by_name('.text')
    ops = code.data()

    addr = code['sh_addr']
    output('+', 2, f'Base address: {addr}')

    if mode == 32:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif mode == 64:
        md = Cs(CS_ARCH_X86, CS_MODE_64) 
    output('+', 2, 'Architecture: x86.')
    output('+', 2, f'Mode : {mode} bit.')

    assembly_code = []
    for i in md.disasm(ops, addr):        
        instruction = f'0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}'
        if VERBOSE:
            output('info', 2, instruction)
        assembly_code.append(instruction)
    output('+', 1, 'Retrieved assembly code.')
    return assembly_code