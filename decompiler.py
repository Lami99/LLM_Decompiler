"""
Python Script used to communicate with Ghidra's API.
It will decompile all the functions of a defined binary and
save results into decompiled_output.c
"""

import sys
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Communicates with Decompiler Interface
decompinterface = DecompInterface()

# Open Current Program
decompinterface.openProgram(currentProgram);

# Get Binary Functions
functions = currentProgram.getFunctionManager().getFunctions(True)

# Markers for function start and end
function_start_marker = "----- START OF FUNCTION: {name} -----"
function_end_marker = "----- END OF FUNCTION: {name} -----"

# Iterates through all functions in the binary and decompiles them
# Then prints the Pseudo C Code
with open("decompiled_output.c", "w") as output_file:
    for function in list(functions):
        function_name = function.getName()

        # Add a marker and a comment with the name of the function at the start
        output_file.write(function_start_marker.format(name=function_name) + "\n")
        output_file.write("// Function: {}\n".format(function_name))

        # Decompile each function
        decompiled_function = decompinterface.decompileFunction(function, 0, ConsoleTaskMonitor())
        # Print Decompiled Code
        output_file.write(decompiled_function.getDecompiledFunction().getC())

        # Add a marker at the end of the function
        output_file.write("\n" + function_end_marker.format(name=function_name) + "\n\n")