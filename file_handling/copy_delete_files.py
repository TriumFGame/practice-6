import os
import shutil

source_file = "sample.txt"
backup_file = "sample_backup.txt"

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print(f"File copied from {source_file} to {backup_file}")

file_to_delete = backup_file

if os.path.exists(file_to_delete):
    print(f"Path '{file_to_delete}' exists.")
    
    if os.access(file_to_delete, os.W_OK):
        print(f"We have write access to '{file_to_delete}'. Deleting now...")
        os.remove(file_to_delete)
        print(f"File '{file_to_delete}' deleted successfully.")
    else:
        print(f"Permission denied: cannot delete '{file_to_delete}'.")
else:
    print(f"File '{file_to_delete}' does not exist.")