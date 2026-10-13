import os

filename = "sample.txt"

if os.path.exists(filename):
    print("--- File Contents ---")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Total number of lines in '{filename}': {len(lines)}")
else:
    print(f"File {filename} does not exist. Please run write_files.py first.")