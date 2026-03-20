# DSA STEP 8 PRACTICE: Two Pointers Technique
# Type each exercise 3-4 times until it's muscle memory

# Pattern 1: Opposite Ends - Two Sum Sorted
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Exercise 8.1: Check palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Exercise 8.2: Remove duplicates from sorted array
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

# Pattern 2: Fast & Slow Pointers
def find_middle(nums):
    slow = fast = 0
    while fast < len(nums) and fast + 1 < len(nums):
        slow += 1
        fast += 2
    return nums[slow]

# Exercise 8.3: Container With Most Water
def max_area(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test
print(two_sum_sorted([2, 7, 11, 15], 9))
print(is_palindrome("racecar"))
nums = [1, 1, 2, 2, 3, 4]
print(remove_duplicates(nums))


