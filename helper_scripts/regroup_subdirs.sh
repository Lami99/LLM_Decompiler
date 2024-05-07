#!/bin/bash

# Script Name: regroup_subdirs.sh
# Description:
# This script takes two arguments: a directory path and a substring.
# It performs the following operations:
# 1. Validates the provided input to ensure that a directory path and a substring are given.
# 2. Navigates to the specified directory.
# 3. Searches for all subdirectories that start with the given substring.
# 4. Creates a new directory named after the substring if it doesn't already exist.
# 5. Moves all the identified subdirectories into this newly created directory.
# Usage: ./regroup_subdirs.sh <directory_path> <substring>
# Example: ./regroup_subdirs.sh /path/to/parent-directory substring

# Check for correct number of arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory_path> <substring>"
    exit 1
fi

# Assign arguments to variables for clarity
directory_path=$1
substring=$2

# Navigate to the directory, exit with an error if it doesn't exist
cd "$directory_path" || { echo "Directory not found: $directory_path"; exit 1; }

# Create a target directory named after the substring if it does not exist
target_directory="${substring}"
if [ ! -d "$target_directory" ]; then
    echo "Creating directory named after substring: $target_directory"
    mkdir "$target_directory"
else
    echo "Directory already exists: $target_directory"
fi

# Find subdirectories starting with the substring and move them to the target directory
# The ! -name "$substring" prevents moving the target directory into itself if it matches the substring criteria
find . -maxdepth 1 -type d -name "${substring}*" ! -name "$substring" -exec mv {} "$target_directory/" \;

echo "Subdirectories have been regrouped into $target_directory."
