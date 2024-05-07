import os
import shutil
import re

"""
This script performs two main functions on the directory structure under 'Dataset/juliet-test-suite-c-master/testcases':
1. Filters out directories that do not correspond to specific CWE numbers specified in the list 'cwe_numbers_to_keep'.
2. Recursively processes all C/C++ source code files within the retained directories, replacing certain predefined strings in the main function of each source file.

The purpose of the script is to clean up the dataset by keeping only relevant directories and standardizing certain text in source files to hide wheras we are calling the bad or good function.
"""

def filter_directories(base_path, cwe_numbers):
    cwe_set = set(cwe_numbers)
    for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
        for dirname in dirnames:
            if dirname.startswith("CWE"):
                cwe_number = dirname.split('_')[0][3:]
                if cwe_number not in cwe_set:
                    full_dir_path = os.path.join(dirpath, dirname)
                    shutil.rmtree(full_dir_path)
                    print(f"Removed directory: {full_dir_path}")

def process_files(base_path):
    string_to_replace = {
        r'Calling good\(\)\.\.\.': 'calling routine()...',
        r'Finished good\(\)': 'Finished routine()',
        r'Calling bad\(\)\.\.\.': 'calling routine()...',
        r'Finished bad\(\)': 'Finished routine()'
    }
    patterns = {re.compile(k): v for k, v in string_to_replace.items()}
    for dirpath, dirnames, filenames in os.walk(base_path):
        for filename in filenames:
            if filename.endswith(('.c', '.cpp')):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                modified = False
                for pattern, replacement in patterns.items():
                    if pattern.search(content):
                        content = pattern.sub(replacement, content)
                        modified = True
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(content)
                        print(f"Modified file: {file_path}")

# Directory relative path
base_directory_path = "Dataset/juliet-test-suite-c-master/testcases"

# List of CWE numbers to keep
cwe_numbers_to_keep = ["78", "122", "134", "197", "242", "367", "391", "401", "415", "416", "457", "467", "468", "476", "478", "480", "482", "561", "562", "563", "590", "835"]

# Filter directories
filter_directories(base_directory_path, cwe_numbers_to_keep)

# Process the files
process_files(base_directory_path)
