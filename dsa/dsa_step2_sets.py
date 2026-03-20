# DSA STEP 2 PRACTICE: Sets
# Type each exercise 3-4 times until it's muscle memory

# Exercise 2.1: Basic set operations
seen = set()
seen.add(1)
seen.add(2)
seen.add(1)  # Duplicate, won't add
print(seen)
print(1 in seen)

# Exercise 2.2: Find duplicates
numbers = [1, 2, 3, 2, 4, 3, 5]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
print(duplicates)

# Exercise 2.3: Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 4, 5]
unique = list(set(numbers))
print(unique)

# Exercise 2.4: Set comprehension
numbers = [1, 2, 3, 4, 5]
squares = {num * num for num in numbers}
print(squares)

# Exercise 2.5: Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
print(f"Union: {union}")
print(f"Intersection: {intersection}")
print(f"Difference: {difference}")

# LeetCode Pattern: Contains Duplicate
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test it
print(contains_duplicate([1, 2, 3, 1]))  # True
print(contains_duplicate([1, 2, 3, 4]))  # False


