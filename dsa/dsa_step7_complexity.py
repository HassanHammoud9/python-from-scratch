# DSA STEP 7 PRACTICE: Time & Space Complexity
# Type each exercise 3-4 times and identify the complexity

# O(1) - Constant time
def get_first(arr):
    return arr[0]

# O(n) - Linear time
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# O(log n) - Logarithmic time
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

# Exercise: Identify time complexity
def example1(arr):
    return arr[0]  # O(?)

def example2(arr):
    total = 0
    for num in arr:
        total += num
    return total  # O(?)

def example3(arr):
    for i in arr:
        for j in arr:
            print(i, j)  # O(?)

# Exercise: Optimize from O(n²) to O(n)
def find_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Optimized O(n) version
def find_duplicate_fast(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
test_arr = [1, 2, 3, 2, 4]
print(find_duplicate_slow(test_arr))
print(find_duplicate_fast(test_arr))


