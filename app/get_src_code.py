from elftools.elf.elffile import ELFFile
from capstone import *

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
# Function to print the assembly code from the .text section
#
def get_assembly(elffile):
    code = elffile.get_section_by_name('.text')
    ops = code.data()
    addr = code['sh_addr']
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    for i in md.disasm(ops, addr):        
        print(f'0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}')

#
# Main function
#
def get_src_code(info, binary):
    elffile = ELFFile(binary)
    sections = {}

    if info['format'] == 'ELF':
        sections = get_elf_binary_sections(elffile, sections)
    
    if len(sections) > 1 and '.text' in sections.values():
        get_assembly(elffile)

    return 1