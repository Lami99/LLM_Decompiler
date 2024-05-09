# Reverse Engineering AI Enhanced Tool (Decompilation/Reconstruction/Scanning automation)

<ins> **Description** </ins>

This tool is designed to streamline and automate the process of decompiling executables—particularly those with stripped binaries—using a command-line interface to eliminate the slowdowns associated with GUI-based decompilation. It harnesses the power of Language Model Systems (LLMs), such as GPT-4, to reconstruct, enhance, and analyze decompiled code. This capability is critical for detecting bugs and vulnerabilities within binaries and is broadly applicable to various reverse engineering tasks. LLMs have demonstrated effectiveness akin to static analyzers on source code, which prompted the exploration of their limitations and capabilities with compiled stripped code.

<ins> **Experiment Validating Hypothesis** </ins>

Motivated by existing research on the effectiveness of LLMs in analyzing source code, we sought to quantify the performance of the GPT-4 model on binary vulnerability analysis, drawing parallels to studies like those documented in "On the capability of static code analysis to detect security vulnerabilities", which examined static analyzers on the Juliet Test Suite. The Juliet Test Suite was chosen because it provides a comprehensive set of test cases specifically designed to benchmark the accuracy and effectiveness of vulnerability detection tools across a wide range of programming errors.

The experiment involved scanning code in two phases:

-Direct analysis of decompiled outputs.
-Analysis of source code post-enhancement and reconstruction, aimed at addressing typical decompilation flaws.

This process was informed by previous methodologies that sought to improve the accuracy of static analyzers by refining decompiled output before analysis.

<ins> **Preliminary Results** </ins>

-Enhanced decompiled binary analysis using LLMs outperformed traditional methods across all evaluated metrics.
-Tools based on LLM detection demonstrated higher efficacy in identifying existing bugs but incurred more false positives compared to conventional static analyzers.

Conclusion:

LLM-based tools show promise for integration into development stacks, particularly where the cost of false positives is manageable. Such tools can significantly aid developers, especially those at the entry level, by automating the enhancement of decompiled code and providing insightful vulnerability assessments.
Capabilities:

<ins> **The command-line tool offers several functionalities** </ins>

    Code Recovery: Transforms binary files into enhanced, high-quality decompiled code in the user's preferred programming language, closely approximating the original source code's structure and logic.
    Vulnerability Reporting: Generates detailed reports identifying potential security weaknesses in the original binary.
    Exploit Script Generation: Provides skeleton scripts that can serve as a basis or inspiration for crafting proof-of-concept exploits for identified bugs.
    Handling Long Code Bases: Efficiently processes extensive code bases, making it suitable for comprehensive software projects.

<ins> **Setup Guide ** </ins>
1. Decompiler setup
    Download Ghidra:
        Visit the Ghidra release page https://github.com/NationalSecurityAgency/ghidra/releases and download the zip file named ghidra_release_PUBLIC_refNumber.zip from the assets of the selected release.

    Extract Ghidra:
        Unzip the downloaded file into the Decompiler directory ensuring that the contents are directly placed under this directory.

    Script Setup:
        Copy all scripts from Decompiler/decompilation_scripts to Decompiler/ghidra_11.0.1_PUBLIC/Ghidra/Features/Decompiler/ghidra_scripts.

    Update Ghidra Path:
        If using a Ghidra release different from 11.0.1, update the GHIDRA_PATH in the Decompiler/gd_decomp.sh script to match the version you have installed.

2. Change the openai key with you own key in the .env file
3. Dataset setup(optional: only if you want reproduce or extend the experiement described above)


<ins> **Usage and Script Descriptions** </ins>
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

    Description: Enhances large decompiled code bases using the OpenAI GPT-4 model, which can be switched to any other OpenAI model as needed. This script focuses on improving readability and maintainability by adding descriptive comments and renaming functions and variables.
    Usage: Execute the script by providing the path to a JSON file containing decompiled function data:

    python large_code_base_reconstruction.py path_to_decompiled_output_json

7. llm_d.py

    Description: Utilizes the OpenAI GPT-4 model to analyze decompiled code, identifying and cataloging vulnerabilities with an emphasis on minimizing false positives to ensure reliable security assessments. The model used can be adjusted to any other OpenAI model to suit different analysis needs.
    Usage: This script requires an input filename and outputs a detailed vulnerability report:

    python llm_d.py input_file_name

8. llm_f.py

    Description: Employs AI, specifically the OpenAI GPT-4 model, to filter out irrelevant functions from decompiled source code, retaining only those functions that are critical for understanding the code’s logic. This process aids in focusing subsequent analyses and can be adapted to use different OpenAI models.
    Usage: Run the script by specifying the path to the decompiled source code file:

    python llm_f.py path_to_decompiled_source_code

9. llm_r.py

    Description: Uses the OpenAI GPT-4 model to enhance the clarity of decompiled source code by intelligently renaming variables and adding explanatory comments. This enhancement aids in subsequent vulnerability assessments and maintenance, and the script can accommodate other OpenAI models as required.
    Usage: To enhance decompiled code, provide the filename of the decompiled code:

    python llm_r.py decompiled_code_file

Other usefull scripts are under helper_scripts directory, that can be usefull for batch analysis 