import os

nested_path = "parent_dir/child_dir/grandchild_dir"
os.makedirs(nested_path, exist_ok=True)
print(f"Nested directories created: {nested_path}")

path_to_check = "parent_dir"
print(f"\nAccess check for '{path_to_check}':")
print(f"Exists: {os.path.exists(path_to_check)}")
print(f"Readable: {os.access(path_to_check, os.R_OK)}")
print(f"Writable: {os.access(path_to_check, os.W_OK)}")
print(f"Executable: {os.access(path_to_check, os.X_OK)}")

sample_path = "parent_dir/child_dir/example.txt"
with open(sample_path, 'w') as f: f.write("test")

if os.path.exists(sample_path):
    print(f"\nPath '{sample_path}' exists.")
    directory_portion = os.path.dirname(sample_path)
    filename_portion = os.path.basename(sample_path)
    print(f"Directory portion: {directory_portion}")
    print(f"Filename portion: {filename_portion}")

print("\n--- Listing Contents of current directory ---")
base_dir = "."
all_items = os.listdir(base_dir)

directories = [d for d in all_items if os.path.isdir(os.path.join(base_dir, d))]
files = [f for f in all_items if os.path.isfile(os.path.join(base_dir, f))]

print(f"Only Directories: {directories}")
print(f"Only Files: {files}")
print(f"All items: {all_items}")