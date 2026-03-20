# DSA STEP 9 PRACTICE: Sliding Window Technique
# Type each exercise 3-4 times until it's muscle memory

# Pattern 1: Fixed Window Size
def max_sum_subarray(nums, k):
    if len(nums) < k:
        return 0
    
    # Calculate first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Exercise 9.1: Average of subarrays
def average_subarray(nums, k):
    if len(nums) < k:
        return []
    
    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum / k)
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        result.append(window_sum / k)
    
    return result

# Pattern 2: Variable Window Size
def longest_substring_no_repeat(s):
    char_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Exercise 9.2: Minimum window substring pattern
def min_window(s, t):
    if not s or not t:
        return ""
    
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    
    left = 0
    have = 0
    need_count = len(need)
    min_len = float('inf')
    result = ""
    
    for right in range(len(s)):
        if s[right] in need:
            need[s[right]] -= 1
            if need[s[right]] == 0:
                have += 1
        
        while have == need_count:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
            
            if s[left] in need:
                if need[s[left]] == 0:
                    have -= 1
                need[s[left]] += 1
            left += 1
    
    return result

# Test
print(max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))
print(longest_substring_no_repeat("abcabcbb"))


