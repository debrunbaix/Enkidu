def output(type, indent, message):
    tab = '    ' * indent if indent > 0 else ''
    print(f'{tab}[{type}] {message}')