RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NO_COLOR = '\033[0m'

TITLE = YELLOW + '''
_______________________________________________


 ███████╗███╗   ██╗██╗  ██╗██╗██████╗ ██╗   ██╗
 ██╔════╝████╗  ██║██║ ██╔╝██║██╔══██╗██║   ██║
 █████╗  ██╔██╗ ██║█████╔╝ ██║██║  ██║██║   ██║
 ██╔══╝  ██║╚██╗██║██╔═██╗ ██║██║  ██║██║   ██║
 ███████╗██║ ╚████║██║  ██╗██║██████╔╝╚██████╔╝
 ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═════╝  ╚═════╝ 

                                    .DEBRUNBAIX             
_______________________________________________
    ''' + NO_COLOR

def output(log_type, indent, message):
    tab = '    ' * indent if indent > 0 else ''
    if log_type == '+':
        log_type = GREEN + log_type + NO_COLOR
    elif log_type == '-':
        log_type = RED + log_type + NO_COLOR
    else:
        log_type = YELLOW + 'info' + NO_COLOR

    print(f'{tab}[{log_type}] {message}')