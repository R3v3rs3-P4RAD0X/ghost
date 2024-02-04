#!/usr/bin/python

import hashlib
import sys

def get_arguments():
    if len(sys.argv) != 3:
        print("Usage: python hash_compare.py <file1> <file2>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def hash_file(file):
    try:
        with open(file, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        print(f"File {file} not found")
        sys.exit(1)

def main():
    file1, file2 = get_arguments()
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    if hash1 == hash2:
        print(f"Files {file1} and {file2} are identical")
    else:
        print(f"Files {file1} and {file2} are different")

if __name__ == "__main__":
    main()
