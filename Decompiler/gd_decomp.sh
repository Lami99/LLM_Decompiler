#!/bin/bash

#script to automatically decompile and output source code of a binary with ghidra

GHIDRA_PATH=./ghidra_11.0.1_PUBLIC
DECOMPILE_SCRIPT_PATH=.

if [ "$#" -ne    2 ]
then 
    echo "$0 <binary path> <output source path>"
    exit
fi

echo "path to decompile script:" $DECOMPILE_SCRIPT_PATH

#remove gpr and rep files first (CAREFUL!)
rm -rf *.gpr *.rep

#/path/to/ghidra/support/analyzeHeadless [project_location] [project_name] -import [path_to_executable] -postScript [script_name] [script_options] -deleteProject

echo "running command:"
echo time $GHIDRA_PATH/support/analyzeHeadless . tmp_ghidra_project -import $1  -postscript $DECOMPILE_SCRIPT_PATH/decompiler.py $2
time $GHIDRA_PATH/support/analyzeHeadless . tmp_ghidra_project -import $1  -scriptPath $DECOMPILE_SCRIPT_PATH -postscript decompiler.py $2

