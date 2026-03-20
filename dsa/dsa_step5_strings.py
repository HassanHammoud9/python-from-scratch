# DSA STEP 5 PRACTICE: String Manipulation
# Type each exercise 3-4 times until it's muscle memory

# Exercise 5.1: Basic string operations
s = "Python"
print(s[0])
print(s[-1])
print(s[1:4])

# Exercise 5.2: String building efficiently
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)

# Exercise 5.3: String manipulation
s = "  hello world  "
s = s.strip()
s = s.replace(" ", "-")
print(s)

# Exercise 5.4: Check palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("race car"))
print(is_palindrome("hello"))

# Exercise 5.5: Efficient string building
# BAD: O(n²)
result = ""
for char in "hello":
    result += char

# GOOD: O(n)
result = []
for char in "hello":
    result.append(char)
result = "".join(result)
print(result)

# BEST: List comprehension
result = "".join([char for char in "hello"])
print(result)

# LeetCode Pattern: Reverse words in string
def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])

# Test it
print(reverse_words("the sky is blue"))  # "blue is sky the"


