from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list: {numbers}")

squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers (map): {squared}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (filter): {evens}")

total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers (reduce): {total_sum}")

max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Max number (reduce): {max_num}")