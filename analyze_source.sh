#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path_to_source_code"
    exit 1
fi

basePath="." 
source_path=$(realpath "$1")
source_name_with_extension=$(basename "$source_path")
source_name=$(basename "$source_path" | cut -f 1 -d '.')  # Name without the .c extension

# Copy the source code to the current directory 
echo "Preparing source file for analysis..."
cp "$source_path" "$basePath/$source_name_with_extension"

# Generate a vulnerability report for the source code
echo "Generating vulnerability report for $source_name..."
python llm_d.py "$basePath/$source_name_with_extension"  # Use the copied file
echo "Vulnerability analysis completed."

# Directory for outputs
outputDir="${basePath}/results/${source_name}/source_analysis"
mkdir -p "$outputDir"

# Move the generated vulnerability report to the designated output directory
mv "${basePath}/${source_name}_vulnerabilities.txt" "$outputDir"

# Clean up: remove the copied source file from "." 
echo "Cleaning up..."
mv "$basePath/$source_name_with_extension" "$outputDir"
rm "$basePath/$source_name_with_extension"

echo "Analysis complete. All files saved to ${outputDir}"
