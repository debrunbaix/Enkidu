from elftools.elf.elffile import ELFFile

from app.output_functions import output
# from app.analyse.sections import get_rodata
from app.analyse.assembly import get_assembly_code

def get_elf_binary_sections(elffile, sections: dict) -> dict:
    """
        put binary's sections in an object
    """
    for section in elffile.iter_sections():
        sections.update({
            hex(section['sh_addr']): section.name
        })
    return sections

def analyse(info: dict, binary, VERBOSE: bool):
    """
    Analyse an ELF binary file and extract relevant sections.

    This function takes in the binary information, opens it as an ELF file,
    and extracts the necessary sections based on the provided format.
    It will print verbose output if the VERBOSE flag is set.

    Parameters:
    - info (dict): Information about the binary, including its format and bitness.
    - binary (file-like object): The binary file to be analyzed.
    - VERBOSE (bool): A flag to enable verbose output.

    Returns:
    - tuple: Contains the assembly code and read-only data section (rodata) if available.
    """
    output('+', 0, 'Analysing binary:')
    elffile = ELFFile(binary)
    sections = {}

    if info['format'] == 'ELF':
        sections = get_elf_binary_sections(elffile, sections)
        if VERBOSE:
            output('info', 1, sections)
        output('+', 1, 'Extracted binary sections.')
    else :
        output('-', 1, 'Please provide ELF binary.')
    
    if len(sections) > 1:
        if '.text' in sections.values():
            assembly_code = get_assembly_code(elffile, info['bit'], VERBOSE)
        
        # if '.rodata' in sections.values():
        #     rodata = get_rodata(elffile, VERBOSE)

    return assembly_code #, rodata