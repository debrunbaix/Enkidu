from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection
from capstone import *
from output_functions import output

import sys
import json

#
# Function to put binary's sections in an object
#
def get_elf_binary_sections(elffile, sections):
    for section in elffile.iter_sections():
        sections.update({
            hex(section['sh_addr']): section.name
        })
    return sections

#
# Function to get the assembly code from the .text section
#
def get_assembly(elffile, mode):
    print('    [+] Getting assembly code.')
    code = elffile.get_section_by_name('.text')
    ops = code.data()

    addr = code['sh_addr']
    print(f'        [+] First address : {addr}')

    if mode == 32:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif mode == 64:
        md = Cs(CS_ARCH_X86, CS_MODE_64) 
    print(f'        [+] arch : x86\n        [+] {mode} bit.')

    assembly_code = []
    for i in md.disasm(ops, addr):        
        instruction = f'0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}'
        assembly_code.append(instruction)
    return assembly_code

#
# Function to get .rodata's content.
#
def get_rodata_sections(elffile):
    rodata = elffile.get_section_by_name('.rodata')
    ops = rodata.data()
    addr = rodata['sh_addr']
    
    try:
        decoded_strings = ops.decode('ascii', 'replace')
        print("Contents of .rodata section:")
        offset = 0
        for line in decoded_strings.split('\x00'):  # Split sur les null bytes
            if line:
                readable_line = ''.join((char if 32 <= ord(char) <= 126 else '.') for char in line)
                print(f"0x{addr+offset:x}: {readable_line}")
            offset += len(line) + 1  # +1 pour le null byte qui a été enlevé par split
    except UnicodeDecodeError as e:
        print(f"[-] Error decoding .rodata: {e}")

#
# Function to get relocations informations.
#
def get_relocations(elffile):
    print('\nrellocation')
    for section in elffile.iter_sections():
        if isinstance(section, RelocationSection):
            print(f'{section.name}:')
            symbol_table = elffile.get_section(section['sh_link'])
            for relocation in section.iter_relocations():
                symbol = symbol_table.get_symbol(relocation['r_info_sym'])
                addr = hex(relocation['r_offset'])
                print(f'    {symbol.name} {addr}')

def save_assembly_to_file(assembly_instructions, filename):
    with open(filename, 'w') as file:
        for instruction in assembly_instructions:
            file.write(instruction + "\n")

#
# Main function
#
def get_src_code(info, binary):
    output('+', 0, 'Getting source code.')
    elffile = ELFFile(binary)
    sections = {}

    # Is the binary an ELF
    if info['format'] == 'ELF':
        sections = get_elf_binary_sections(elffile, sections)
        output('+', 1, 'Get binary\'s sections done.')
    else :
        print('-', 1, 'Please provide ELF binary.')
    
    if len(sections) > 1:
        # get_relocations(elffile)
        if '.text' in sections.values():
            assembly_code = get_assembly(elffile, info['bit'])
            save_assembly_to_file(assembly_code, f'{info["name"]}_assembly_code.txt')
        
        if '.rodata' in sections.values():
            get_rodata_sections(elffile)

    return 1