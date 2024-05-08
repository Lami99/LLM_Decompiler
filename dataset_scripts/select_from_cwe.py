import os
import random
import shutil
import sys

def select_files(base_dir, mirror_dir, save_dir, suffix_bad='-bad', suffix_good='-good', num_files=5):
    """
    Selects a random set of files from a given directory and finds their corresponding 'good' files
    in another directory. Selected files are then copied to a specified directory.
    
    Args:
    base_dir (str): Path to the directory containing 'bad' files.
    mirror_dir (str): Path to the directory containing 'good' files.
    save_dir (str): Path to the directory where selected files will be saved.
    suffix_bad (str): Suffix of the 'bad' files.
    suffix_good (str): Suffix of the 'good' files.
    num_files (int): Number of files to randomly select.

    Outputs:
    Copies selected 'bad' and corresponding 'good' files to the save_dir directory.
    """
    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # List all files in the base directory that end with the specified bad suffix
    all_bad_files = [f for f in os.listdir(base_dir) if f.endswith(suffix_bad)]
    
    # Randomly select a subset of these files
    selected_bad_files = random.sample(all_bad_files, num_files)
    
    # Prepare the corresponding "good" file names
    selected_good_files = [f.replace(suffix_bad, suffix_good) for f in selected_bad_files]
    
    # Verify that the corresponding "good" files exist in the mirror directory
    existing_good_files = [f for f in selected_good_files if f in os.listdir(mirror_dir)]
    
    # Copy selected files to the save directory
    for file in selected_bad_files:
        shutil.copy(os.path.join(base_dir, file), os.path.join(save_dir, file))
    
    for file in existing_good_files:
        shutil.copy(os.path.join(mirror_dir, file), os.path.join(save_dir, file))
    
    print("Files have been copied to:", save_dir)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python select_from_cwe.py <base_directory> <mirror_directory>")
        sys.exit(1)
    
    base_directory = sys.argv[1]
    mirror_directory = sys.argv[2]
    save_directory = '../selected_binaries'  # Set the directory where selected files will be saved
    
    select_files(base_directory, mirror_directory, save_directory)
