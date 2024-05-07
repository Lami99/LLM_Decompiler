Results of every single analysis will be saved in this directory following the naming convention:

results/

└── [item_name]/                                 # Folder named after the executable or source (e.g., myprogram or mysource)

    ├── enhanced_executable_analysis/            # For enhanced analysis of executables

    │   ├── [item_name].exe                      # Original executable copied

    │   ├── [item_name]_decompiled.c             # Decompiled code

    │   ├── [item_name]_decompiled_filtered.c    # Filtered decompiled code

    │   ├── [item_name]_decompiled_filtered_enhanced.c      # Enhanced decompiled code

    │   └── [item_name]_decompiled_filtered_enhanced_vulnerabilities.txt  # Vulnerability report

    ├── executable_analysis/                     # For basic analysis of executables

    │   ├── [item_name]_decompiled.c             # Decompiled code

    │   └── [item_name]_decompiled_vulnerabilities.txt      # Vulnerability report

    └── source_analysis/                         # For analysis of source code
    
        ├── [item_name].c                        # Source code file

        └── [item_name]_vulnerabilities.txt      # Vulnerability report
