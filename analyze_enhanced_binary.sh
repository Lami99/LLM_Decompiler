#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path_to_executable"
    exit 1
fi

# The base path for operations
basePath="." 

# Resolve the absolute path of the executable and its base name
executable_path=$(realpath "$1")
executable_name=$(basename "$executable_path" | cut -f 1 -d '.')

# Step 1: Decompile the executable
echo "Starting decompilation of $executable_name..."
cd "$basePath"
./decompile_pipe.sh "$executable_path"
echo "Decompilation completed."

# Step 2.0: filter the decompiled code
echo "filtering the decompiled code of $executable_name..."
python llm_f.py "${executable_name}_decompiled.c"
echo "Code filtering completed."

# Step 2.1: Enhance the decompiled code
echo "Enhancing the decompiled code of $executable_name..."
python llm_r.py "${executable_name}_decompiled_filtered.c"
echo "Code enhancement completed."

# Step 3: Generate a vulnerability report
echo "Generating vulnerability report for $executable_name..."
python llm_d.py "${executable_name}_decompiled_filtered_enhanced.c"
echo "Vulnerability analysis completed."

# Create a directory for all outputs
outputDir="${basePath}/results/${executable_name}/enhanced_executable_analysis"
mkdir -p "$outputDir"

# Copy the original executable to the new directory
cp "${executable_path}" "$outputDir"

# Move the generated files to the new directory
mv "${basePath}/${executable_name}_decompiled.c" "$outputDir"
mv "${basePath}/${executable_name}_decompiled_filtered.c" "$outputDir"
mv "${basePath}/${executable_name}_decompiled_filtered_enhanced.c" "$outputDir"
mv "${basePath}/${executable_name}_decompiled_filtered_enhanced_vulnerabilities.txt" "$outputDir"

echo "Analysis complete. All files saved to ${outputDir}"
