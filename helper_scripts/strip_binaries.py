"""
Strip Binary Files

Description:
This script recursively traverses a directory provided via command line argument and applies the 'strip' command to all binary executable files found.
The 'strip' command removes symbols and debugging information from binary executables, which can reduce their size.

Usage:
python strip_binaries.py <directory_path>

Example:
python strip_binaries.py /path/to/directory

Dependencies:
This script requires the 'file' and 'strip' utilities, typically available on Unix-like systems. It is intended to run in environments where these commands are supported.
"""

import os
import subprocess
import sys

def is_binary_executable(file_path):
    try:
        result = subprocess.run(['file', file_path], stdout=subprocess.PIPE, text=True)
        return 'executable' in result.stdout
    except Exception as e:
        print(f"Failed to check file type: {e}")
        return False

def strip_binaries(base_path):
    for dirpath, dirnames, filenames in os.walk(base_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if is_binary_executable(file_path):
                try:
                    print(f"Stripping binary: {file_path}")
                    subprocess.run(['strip', file_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error stripping file {file_path}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>")
        sys.exit(1)
    base_directory_path = sys.argv[1]
    strip_binaries(base_directory_path)
