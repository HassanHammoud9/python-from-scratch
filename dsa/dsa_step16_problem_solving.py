# DSA STEP 16 PRACTICE: Problem-Solving Framework
# Use this template for every LeetCode problem

def solve_problem(input):
    # Step 1: Handle edge cases
    if not input:
        return []
    
    # Step 2: Initialize variables
    result = []
    seen = set()
    
    # Step 3: Main logic
    for item in input:
        # Process item
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    # Step 4: Return result
    return result

# Exercise 16.1: Find all numbers that appear twice
# Input: [4,3,2,7,8,2,3,1]
# Output: [2,3]

def find_duplicates(nums):
    # Step 1: Edge case
    if not nums:
        return []
    
    # Step 2: Initialize
    seen = {}
    duplicates = []
    
    # Step 3: Main logic
    for num in nums:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen[num] = True
    
    # Step 4: Return
    return duplicates

# Exercise 16.2: Find missing number
# Input: [3,0,1]
# Output: 2

def missing_number(nums):
    # Step 1: Edge case
    if not nums:
        return 0
    
    # Step 2: Initialize
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    # Step 3: Main logic (already done)
    # Step 4: Return
    return expected_sum - actual_sum

# Exercise 16.3: Move zeros to end
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

def move_zeros(nums):
    # Step 1: Edge case
    if not nums:
        return
    
    # Step 2: Initialize
    slow = 0
    
    # Step 3: Main logic
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    
    # Step 4: Return (modify in-place)

# Test
print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(missing_number([3, 0, 1]))
test_nums = [0, 1, 0, 3, 12]
move_zeros(test_nums)
print(test_nums)


