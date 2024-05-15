from elftools.elf.elffile import ELFFile
from elftools.elf.relocation import RelocationSection
from capstone import *
from app.output_functions import output

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
    output('+', 1, 'Getting assembly code.')
    code = elffile.get_section_by_name('.text')
    ops = code.data()

    addr = code['sh_addr']
    output('+', 2, f'First address : {addr}')

    if mode == 32:
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    elif mode == 64:
        md = Cs(CS_ARCH_X86, CS_MODE_64) 
    output('+', 2, 'arch : x86.')
    output('+', 2, f'{mode} bit.')

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
        offset = 0
        rodata_list = []
        for line in decoded_strings.split('\x00'):
            if line:
                readable_line = ''.join((char if 32 <= ord(char) <= 126 else '.') for char in line)
                # print(f"0x{addr+offset:x}: {readable_line}")
                if readable_line != '.':
                    rodata_list.append(readable_line)

            offset += len(line) + 1
    except UnicodeDecodeError as e:
        print(f"[-] Error decoding .rodata: {e}")
    return rodata_list

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

    if info['format'] == 'ELF':
        sections = get_elf_binary_sections(elffile, sections)
        output('+', 1, 'Get binary\'s sections done.')
    else :
        print('-', 1, 'Please provide ELF binary.')
    
    if len(sections) > 1:
        # get_relocations(elffile)
        if '.text' in sections.values():
            assembly_code = get_assembly(elffile, info['bit'])
            # save_assembly_to_file(assembly_code, f'{info["name"]}_assembly_code.txt')
        
        if '.rodata' in sections.values():
            rodata = get_rodata_sections(elffile)

    return assembly_code, rodata