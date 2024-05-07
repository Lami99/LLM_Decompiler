#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 executable_name"
    exit 1
fi

# Store the original directory for later use
original_dir=$(pwd)

# Resolve the absolute path of the executable
executable_path=$(realpath "$1")
executable_name=$(basename "$executable_path")

# Navigate to the Decompiler directory
cd ./Decompiler

# Cleanup any files/directories starting with 'tmp' in the Decompiler directory
find . -name 'tmp*' -exec rm -rf {} +

# Copy the executable into the Decompiler/exec folder and rename it to "exe"
cp "$executable_path" ./exec/exe

# Run the decompilation script
./gd_decomp.sh ./exec/exe /tmp/source.c

# Set the output directory and file name
output_dir="$original_dir"
output_file="${executable_name}_decompiled.c"

# Move the decompiled output to the same directory as the original executable
mv decompiled_output.c "$output_dir/$output_file"

echo "Decompilation finished. Output saved to $output_dir/$output_file"
