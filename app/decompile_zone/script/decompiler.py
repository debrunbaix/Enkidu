#! /usr/bin/env jython
# -*- coding: utf-8 -*-

import os
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

def decompile_function(function, decompiler):

    result = decompiler.decompileFunction(function, 30, ConsoleTaskMonitor())
    
    if result.decompileCompleted():
        return result.getDecompiledFunction().getC(), None
    else:
        return None, result.getErrorMessage()

def main():

    program = currentProgram
    decompiler = DecompInterface()
    decompiler.openProgram(program)

    # Obtenir le chemin de sortie à partir des arguments de script
    args = getScriptArgs()
    if len(args) < 1:
        raise ValueError("No output directory specified")
    output_dir = args[0]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.access(output_dir, os.W_OK):
        raise PermissionError("Permission denied for writing to the output directory: " + output_dir)

    error_log = os.path.join(output_dir, "decompilation_errors.log")

    with open(error_log, "w") as log_file:
        functions = program.getFunctionManager().getFunctions(True)
        for function in functions:
            pseudo_code, error = decompile_function(function, decompiler)
            if pseudo_code:
                output_file = os.path.join(output_dir, function.getName() + ".c")
                with open(output_file, "w") as f:
                    f.write(pseudo_code)
            if error:
                log_file.write("Error decompiling {}: {}\n".format(function.getName(), error))

main()