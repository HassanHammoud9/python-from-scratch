# DSA STEP 10 PRACTICE: Hash Map Patterns
# Type each exercise 3-4 times until it's muscle memory

# Pattern 1: Frequency Counting - Group Anagrams
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

# Exercise 10.1: Find anagram mappings
def find_anagram_mappings(nums1, nums2):
    mapping = {}
    for i, num in enumerate(nums2):
        mapping[num] = i
    
    result = []
    for num in nums1:
        result.append(mapping[num])
    return result

# Pattern 2: Prefix Sum with Hash Map
def subarray_sum_equals_k(nums, k):
    prefix_sum = {0: 1}
    current_sum = 0
    count = 0
    
    for num in nums:
        current_sum += num
        if current_sum - k in prefix_sum:
            count += prefix_sum[current_sum - k]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
    
    return count

# Exercise 10.2: Two Sum (classic)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Exercise 10.3: Longest Consecutive Sequence
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Test
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(two_sum([2, 7, 11, 15], 9))
print(subarray_sum_equals_k([1, 1, 1], 2))
print(longest_consecutive([100, 4, 200, 1, 3, 2]))


