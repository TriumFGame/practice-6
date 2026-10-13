names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print("--- Enumerate Example ---")
for index, name in enumerate(names, start=1):
    print(f"Student {index}: {name}")

print("\n--- Zip Example ---")
for name, score in zip(names, scores):
    print(f"{name} scored {score} points.")

print("\n--- Type Checking & Conversions ---")
value_str = "150"
value_float = 99.99

print(f"Initial types: '{value_str}' is {type(value_str)}, {value_float} is {type(value_float)}")

converted_int = int(value_str)
converted_str = str(value_float)

num_list = [10, 20, 30]
print(f"\nList operations on {num_list}:")
print(f"Length: {len(num_list)}")
print(f"Min: {min(num_list)}")
print(f"Max: {max(num_list)}")
print(f"Sum: {sum(num_list)}")