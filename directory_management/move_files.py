import os
import shutil
from pathlib import Path

os.makedirs("source_folder", exist_ok=True)
os.makedirs("dest_folder", exist_ok=True)
with open("source_folder/test1.txt", "w") as f: f.write("1")
with open("source_folder/test2.log", "w") as f: f.write("2")
with open("source_folder/test3.txt", "w") as f: f.write("3")

print("Finding .txt files in 'source_folder':")
source_path = Path("source_folder")
txt_files = list(source_path.glob("*.txt"))
for file in txt_files:
    print(file.name)

print("\nMoving .txt files to 'dest_folder'...")
for file in txt_files:
    dest_path = Path("dest_folder") / file.name
    shutil.move(str(file), str(dest_path))
    print(f"Moved: {file.name}")

print("Current contents of 'dest_folder':", os.listdir("dest_folder"))