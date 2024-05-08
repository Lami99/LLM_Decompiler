# LLM_Decompiler
Setup Guide

    Download Ghidra:
        Visit the Ghidra release page https://github.com/NationalSecurityAgency/ghidra/releases and download the zip file named ghidra_release_PUBLIC_refNumber.zip from the assets of the selected release.

    Extract Ghidra:
        Unzip the downloaded file into the Decompiler directory ensuring that the contents are directly placed under this directory.

    Script Setup:
        Copy all scripts from Decompiler/decompilation_scripts to Decompiler/ghidra_11.0.1_PUBLIC/Ghidra/Features/Decompiler/ghidra_scripts.

    Update Ghidra Path:
        If using a Ghidra release different from 11.0.1, update the GHIDRA_PATH in the Decompiler/gd_decomp.sh script to match the version you have installed.


Usage and Script Descriptions
1. analyze_all.sh

    Description: Automates the comprehensive analysis of executable files in a specified directory, identifying potential vulnerabilities and providing enhanced code analysis to improve security and maintainability.
    Usage: Execute the script with a directory path to perform analysis on all executables found therein:

    bash

    ./analyze_all.sh /path/to/directory

2. analyze_binary.sh

    Description: Decomposes executable files to source code and performs a vulnerability analysis to identify security risks in the decompiled code.
    Usage: Use this script by specifying the path to an executable:

    bash

    ./analyze_binary.sh path_to_executable

3. analyze_enhanced_binary.sh

    Description: Enhances the decompiled code for readability and maintainability before conducting a detailed vulnerability analysis to ensure comprehensive security assessments.
    Usage: Run the script by providing an executable's path:

    bash

    ./analyze_enhanced_binary.sh path_to_executable
4. analyze_source.sh

    Description: Evaluates source code files for vulnerabilities by generating detailed reports that highlight security flaws, helping developers to make informed security enhancements.
    Usage: Invoke this script with the path to a source code file:

    bash

    ./analyze_source.sh path_to_source_code

5. decompile_pipe.sh

    Description: Streamlines the process of decompiling executables into source code, simplifying the initial stages of security analysis by preparing the code for further inspection.
    Usage: Execute the script by passing the name of the executable:

    bash

    ./decompile_pipe.sh executable_name

6. large_code_base_reconstruction.py

    Description: Uses advanced machine learning models to enhance the readability and maintainability of large decompiled code bases, integrating intelligent naming and detailed commenting.
    Usage: To use this script, provide the path to a JSON file containing decompiled function data:

    python large_code_base_reconstruction path_to_decompiled_output_json

7. llm_d.py

    Description: Applies deep learning techniques to decompiled code to detect and catalog vulnerabilities, focusing on minimizing false positives to provide reliable security assessments.
    Usage: This script requires an input filename and outputs a detailed vulnerability report:

    python llm_d.py input_file_name

8. llm_f.py

    Description: Filters irrelevant functions from decompiled source code using AI, retaining only significant functions that contribute to the logical flow, thus enhancing the focus of further analysis.
    Usage: Run the script by specifying the path to the decompiled source code file:

    python llm_f.py path_to_decompiled_source_code

9. llm_r.py

    Description: Improves the clarity of decompiled source code by intelligently renaming variables and adding explanatory comments, which aids in subsequent vulnerability assessments and code maintenance.
    Usage: To enhance decompiled code, provide the filename of the decompiled code:

    python llm_r.py decompiled_code_file

Other usefull scripts are under helper_scripts directory, that can be usefull for batch analysis 