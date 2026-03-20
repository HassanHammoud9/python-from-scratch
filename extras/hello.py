# My very first Python file.
# I'm keeping the original code below, bugs and all, as a reminder of where I started.
# If you're just starting out: this is what day one looks like. And that's okay.

# --- Original code (with bugs!) ---
# Bug 1: Using "list" as a variable name shadows Python's built-in list()
# Bug 2: The loop uses values as indices instead of actual index positions
# Bug 3: list[i+1] will crash with an IndexError on the last element
#
# print("hello,world!")
# list = [1,2,3,4,5,6,6,8,9,10]
# list.sort()
# print(list)
# is_Duplicate = False
# for i in list:
#     if list[i] == list[i+1]:
#         is_Duplicate = True
#         break
#     else:
#         is_Duplicate = False
# print(is_Duplicate)

# --- Fixed version ---
print("hello, world!")

numbers = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]
numbers.sort()
print(numbers)

is_duplicate = False
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i + 1]:
        is_duplicate = True
        break

print(is_duplicate)

# What changed:
# 1. Renamed "list" to "numbers" so we don't shadow the built-in
# 2. Used range(len(numbers) - 1) to iterate by index properly
# 3. Removed the unnecessary else branch (is_duplicate stays False unless we find one)
# 4. Added "- 1" to avoid IndexError on the last element
