from elftools.elf.elffile import ELFFile

from app.output_functions import output
from app.analyse.assembly import get_assembly_code
from app.analyse.sections import get_rodata, get_data, get_bss

#
# Function to put binary's sections in an object
#
def get_elf_binary_sections(elffile, sections):
    for section in elffile.iter_sections():
        sections.update({
            hex(section['sh_addr']): section.name
        })
    return sections

def analyse(info, binary, VERBOSE):
    output('+', 0, 'Analysing binary:')
    elffile = ELFFile(binary)
    sections = {}

    if info['format'] == 'ELF':
        sections = get_elf_binary_sections(elffile, sections)
        output('info', 1, sections) if VERBOSE else None
        output('+', 1, 'Extracted binary sections.')
    else :
        output('-', 1, 'Please provide ELF binary.')
    
    if len(sections) > 1:
        if '.text' in sections.values():
            assembly_code = get_assembly_code(elffile, info['bit'], VERBOSE)
            # save_assembly_to_file(assembly_code, f'{info["name"]}_assembly_code.txt')
        
        if '.rodata' in sections.values():
            rodata = get_rodata(elffile, VERBOSE)

    return assembly_code, rodata