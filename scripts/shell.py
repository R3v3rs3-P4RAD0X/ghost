#!/usr/bin/python

"""
This script is used to shell out a new directory.

Usage:
    shell.py <dir>
"""

import os
import sys

# Get the directory from the command line
def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    new_dir = sys.argv[1]

    # Check if the directory exists
    if os.path.exists(new_dir):
        print("Directory already exists")
    else:
        os.mkdir(new_dir)
        print("Directory created")
    
    # Change to the new directory
    os.chdir(new_dir)

    # Create a new readme file
    with open("README.md", "w") as f:
        f.write(f"# {new_dir}\n")

    print("Done")
    print(os.getcwd())

if __name__ == "__main__":
    main()
