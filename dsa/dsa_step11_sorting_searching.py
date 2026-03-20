# DSA STEP 11 PRACTICE: Sorting & Searching
# Type each exercise 3-4 times until it's muscle memory

# Built-in Sorting
nums = [3, 1, 4, 1, 5]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# Sort with custom key
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
students.sort(key=lambda x: x[1])
print(students)

# Create new sorted list
sorted_nums = sorted(nums)
print(sorted_nums)

# Exercise 11.1: Sort practice
nums = [64, 34, 25, 12, 22, 11, 90]
nums.sort()
print(nums)

# Binary Search Template
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Exercise 11.2: Search Insert Position
def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Finding Boundaries - First Occurrence
def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Finding Boundaries - Last Occurrence
def find_last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 5))
print(search_insert_position([1, 3, 5, 6], 4))
nums_with_duplicates = [1, 2, 2, 2, 3, 4]
print(find_first_occurrence(nums_with_duplicates, 2))
print(find_last_occurrence(nums_with_duplicates, 2))


