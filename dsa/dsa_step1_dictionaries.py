# DSA STEP 1 PRACTICE: Dictionaries (Hash Maps)
# Type each exercise 3-4 times until it's muscle memory

# Exercise 1.1: Basic dictionary operations
student = {}
student["name"] = "Bob"
student["grade"] = 85
student["subject"] = "Math"
print(student)
print(student["name"])

# Exercise 1.2: Count character frequencies (method 1)
word = "hello"
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Exercise 1.3: Count character frequencies (method 2 - cleaner)
word = "programming"
char_count = {}
for char in word:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# Exercise 1.4: Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared = {num: num * num for num in numbers}
print(squared)

# LeetCode Pattern: Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test it
print(two_sum([2, 7, 11, 15], 9))  # Should return [0, 1]


