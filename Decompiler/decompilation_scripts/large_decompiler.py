import json
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# Initialize Decompiler
decompInterface = DecompInterface()
decompInterface.openProgram(currentProgram)

# Collect all functions
functions = currentProgram.getFunctionManager().getFunctions(True)
function_list = []

for function in functions:
    decompiled_function = decompInterface.decompileFunction(function, 0, ConsoleTaskMonitor())
    function_data = {
        "name": function.getName(),
        "signature": function.getSignature().getPrototypeString(),
        "body": decompiled_function.getDecompiledFunction().getC()
    }
    function_list.append(function_data)

# Write the JSON output to a file
with open("decompiled_output.json", "w") as output_file:
    json.dump(function_list, output_file, indent=2)
