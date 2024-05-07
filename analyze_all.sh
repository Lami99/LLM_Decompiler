#!/bin/bash

# Script Name: analyze_all.sh
# Description: This script recursively finds all executable files in a specified directory
#              and runs two analysis scripts (`analyze_binary.sh` and `analyze_enhanced_binary.sh`)
#              on each executable found.
# Usage: ./analyze_all.sh <directory>
# Example: ./analyze_all.sh /path/to/directory

# Check if the directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Assign the directory to a variable for easier reference
DIRECTORY=$1

# Function to analyze executable files
# Params:
#   $1 - File path of a potential executable to analyze
analyze_files() {
    local file="$1"
    # Check if the file is executable
    if [ -x "$file" ]; then  
        echo "Analyzing $file..."
        # Run the first analysis script
        ./analyze_binary.sh "$file"
        # Run the enhanced analysis script
        ./analyze_enhanced_binary.sh "$file"
    fi
}

# Export the function so it's available to subshells
export -f analyze_files

# Use the find command to locate all files in the directory and its subdirectories
# For each file found, execute the analyze_files function if the file is executable
find "$DIRECTORY" -type f -exec bash -c 'analyze_files "$0"' {} \;

echo "Analysis complete."
