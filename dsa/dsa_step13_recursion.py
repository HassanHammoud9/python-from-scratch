# DSA STEP 13 PRACTICE: Recursion & Backtracking
# Type each exercise 3-4 times until it's muscle memory

# Basic Recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Exercise 13.1: Fibonacci (naive - for learning)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Backtracking Template
def backtrack(candidates, path, result):
    # Base case: solution found
    if len(path) == len(candidates):  # Example condition
        result.append(path[:])  # Copy path
        return
    
    # Try all candidates
    for candidate in candidates:
        if candidate not in path:  # Example validation
            path.append(candidate)  # Make choice
            backtrack(candidates, path, result)
            path.pop()  # Undo choice (backtrack)

# Exercise 13.2: Generate all subsets
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result

# Exercise 13.3: Generate permutations
def permutations(nums):
    result = []
    
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    
    backtrack([])
    return result

# Exercise 13.4: Combination Sum
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result

# Test
print(factorial(5))
print(fibonacci(6))
print(subsets([1, 2, 3]))
print(permutations([1, 2, 3]))
print(combination_sum([2, 3, 6, 7], 7))


