#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path_to_executable"
    exit 1
fi

basePath="." 
executable_path=$(realpath "$1")
executable_name=$(basename "$executable_path" | cut -f 1 -d '.')

# Decompile the executable
echo "Starting decompilation of $executable_name..."
./decompile_pipe.sh "$executable_path"
echo "Decompilation completed."

# Generate a vulnerability report
echo "Generating vulnerability report for $executable_name..."
python llm_d.py "${executable_name}_decompiled.c"
echo "Vulnerability analysis completed."

# Directory for outputs
outputDir="${basePath}/results/${executable_name}/executable_analysis"
mkdir -p "$outputDir"

# Move generated files
mv "${basePath}/${executable_name}_decompiled.c" "$outputDir"
mv "${basePath}/${executable_name}_decompiled_vulnerabilities.txt" "$outputDir"

echo "Analysis complete. All files saved to ${outputDir}"
