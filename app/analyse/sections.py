from app.output_functions import output

def get_rodata(elffile, VERBOSE):
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
                if readable_line != '.':
                    if VERBOSE:
                        output('info', 2, readable_line)
                    rodata_list.append(readable_line)
            offset += len(line) + 1
        output('+', 1, 'Retrieved .rodata section.')
    except UnicodeDecodeError as e:
        output("-", 1, f'Error decoding .rodata: {e}')
    return rodata_list