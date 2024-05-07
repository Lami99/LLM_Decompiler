"""
Count C/C++ Files

Description:
This script counts the number of C and C++ source code files (extensions .c, .cpp, .cc, and .h) in a directory provided via command line argument.
It recursively traverses the directory and all subdirectories to find and count these files.

Usage:
python count_cpp_files.py <directory_path>

Example:
python count_cpp_files.py /path/to/directory

The output is the total number of C/C++ files found in the specified directory.
"""

import os
import sys

def count_c_cpp_files(base_path):
    c_cpp_count = 0
    cpp_extensions = ('.c', '.cpp', '.cc', '.h')
    for dirpath, dirnames, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(cpp_extensions):
                c_cpp_count += 1
    return c_cpp_count

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>")
        sys.exit(1)
    base_directory_path = sys.argv[1]
    file_count = count_c_cpp_files(base_directory_path)
    print(f"Number of C/C++ files: {file_count}")
