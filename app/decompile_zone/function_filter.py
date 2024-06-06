import os

standard_c_functions = [
    "abort", "abs", "acos", "asctime", "asin", "atan", "atan2", "atexit", "atof", "atoi", "atol", "bsearch", 
    "calloc", "ceil", "clock", "cos", "cosh", "ctime", "difftime", "div", "exit", "exp", "fabs", "fclose", 
    "feof", "ferror", "fflush", "fgetc", "fgetpos", "fgets", "floor", "fmod", "fopen", "fprintf", "fputc", 
    "fputs", "fread", "free", "freopen", "frexp", "fscanf", "fseek", "fsetpos", "ftell", "fwrite", "getc", 
    "getchar", "gets", "gmtime", "isalnum", "isalpha", "isascii", "iscntrl", "isdigit", "isgraph", "islower", 
    "isprint", "ispunct", "isspace", "isupper", "isxdigit", "labs", "ldexp", "ldiv", "localtime", "log", "log10", 
    "longjmp", "malloc", "memchr", "memcmp", "memcpy", "memmove", "memset", "mktime", "modf", "perror", "pow", 
    "printf", "putc", "putchar", "puts", "qsort", "raise", "rand", "realloc", "remove", "rename", "rewind", 
    "scanf", "setbuf", "setjmp", "setvbuf", "signal", "sin", "sinh", "sprintf", "sqrt", "srand", "sscanf", "strcat", 
    "strchr", "strcmp", "strcoll", "strcpy", "strcspn", "strftime", "strlen", "strncat", "strncmp", "strncpy", 
    "strpbrk", "strrchr", "strspn", "strstr", "strtod", "strtok", "strtol", "strtoul", "strxfrm", "system", "tan", 
    "tanh", "time", "tmpfile", "tmpnam", "tolower", "toupper", "ungetc", "vfprintf", "vprintf", "vsprintf"
]

no_return = 'return;'

def find_no_return_function(DISASSEMBLY_CODE_PATH, function):
    
    source_file = os.path.join(DISASSEMBLY_CODE_PATH, function + ".c")
    
    with open(source_file, 'r') as f:
        content = f.read()
        return False if no_return in content else True

def function_filter(DISASSEMBLY_CODE_PATH):
    
    filtered_functions = []

    decompiled_functions = os.listdir(DISASSEMBLY_CODE_PATH)
    decompiled_functions = [os.path.splitext(f)[0] for f in decompiled_functions if f.endswith('.c')]

    for function in decompiled_functions:
        if not function.startswith("__") and function not in standard_c_functions and find_no_return_function(DISASSEMBLY_CODE_PATH, function):
            filtered_functions.append(function)

    filtered_functions = [function + ".c" for function in filtered_functions]

    return filtered_functions
    