# DSA STEP 4 PRACTICE: Advanced List Operations
# Type each exercise 3-4 times until it's muscle memory

# Exercise 4.1: List methods
nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
print(nums)

# Exercise 4.2: List slicing mastery
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:7])  # [2, 3, 4, 5, 6]
print(nums[:5])   # [0, 1, 2, 3, 4]
print(nums[5:])   # [5, 6, 7, 8, 9]
print(nums[::-1]) # Reverse: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(nums[::2])  # Every 2nd: [0, 2, 4, 6, 8]

# Exercise 4.3: List comprehension
squares = [i * i for i in range(5)]
print(squares)

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)

# Exercise 4.4: Nested list comprehension
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)

# Exercise 4.5: List operations
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)
nums.reverse()
print(nums)

# LeetCode Pattern: Reverse array in-place
def reverse_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums

# Test it
test_nums = [1, 2, 3, 4, 5]
print(reverse_array(test_nums))


