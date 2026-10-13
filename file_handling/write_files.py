import string
import os

filename = "sample.txt"
with open(filename, 'w') as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
print(f"Data written to {filename}")

with open(filename, 'a') as file:
    file.write("This line was appended later.\n")
print("New line appended.")

my_list = ["Apple", "Banana", "Cherry", "Date"]
list_filename = "fruits.txt"
with open(list_filename, 'w') as file:
    for item in my_list:
        file.write(f"{item}\n")
print(f"List written to {list_filename}")

os.makedirs("alphabet_files", exist_ok=True)
for letter in string.ascii_uppercase:
    with open(f"alphabet_files/{letter}.txt", 'w') as file:
        file.write(f"This is file {letter}.txt\n")
print("26 files (A-Z) generated in 'alphabet_files' directory.")