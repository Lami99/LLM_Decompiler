1. count_cpp_files.py

    Description: Counts the total number of C and C++ source files in a specified directory and its subdirectories, useful for assessing project size or complexity.
    Usage: Run the script by specifying the directory to scan:

    bash

    python count_cpp_files.py /path/to/directory

2. regroup_subdirs.sh

    Description: Organizes subdirectories within a given directory by grouping them into a new directory based on a specified substring, enhancing directory management and project organization.
    Usage: Execute the script by providing a directory path and a substring:

    bash

    ./regroup_subdirs.sh /path/to/parent-directory substring

3. strip_binaries.py

    Description: Recursively strips debugging and symbol information from binary files in a directory, reducing their size and preparing them for production environments or further security analysis.
    Usage: Use the script by providing a path to the directory containing the binaries:

    bash

    python strip_binaries.py /path/to/directory