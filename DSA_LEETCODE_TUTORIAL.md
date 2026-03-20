# DSA & LeetCode Tutorial: Python Edition

The goal: get to the point where you can solve LeetCode problems and handle coding interviews without freezing.

**Prerequisites:** You should be comfortable with the basics (variables, loops, conditionals, lists, functions). If not, start with `PYTHON_TUTORIAL.md` first.

**How to use this:**
- Read each concept, then type out the examples yourself (don't copy paste)
- Complete every practice exercise. Repeat 3 to 4 times until it's muscle memory.
- Solve the LeetCode-style problems at the end of each section
- Only move forward when you can write solutions from memory

Practice files are in the `dsa/` folder. Run them with `python3 dsa/dsa_stepX_*.py`.

---

## PART 1: PYTHON DATA STRUCTURES MASTERY

### STEP 1: Dictionaries (Hash Maps) - Your Secret Weapon

#### Why Dictionaries Matter
Dictionaries are THE most important data structure for LeetCode. They give O(1) average time complexity for lookups, insertions, and deletions.

#### Basic Dictionary Operations
```python
# Creating dictionaries
my_dict = {}
my_dict = {"key": "value"}
my_dict = dict()

# Adding/Updating
my_dict["name"] = "Alice"
my_dict["age"] = 25

# Accessing
value = my_dict["name"]  # Gets "Alice"
value = my_dict.get("name", "default")  # Safer, returns default if key doesn't exist

# Checking existence
if "name" in my_dict:
    print("Key exists")

# Iterating
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
```

#### Keys vs values (revision)
- `if x in my_dict` → checks **keys** only, not values.
- `if x in my_dict.values()` → checks **values** only.

```python
my_dict = {"name": "Alice", "age": 25}
"Alice" in my_dict          # False (Alice is a value, not a key)
"Alice" in my_dict.values() # True
"name" in my_dict           # True
"name" in my_dict.values()  # False
```

#### Time Complexity
- Access: O(1) average
- Insert: O(1) average
- Delete: O(1) average
- Search: O(1) average

**Practice Exercise 1.1:** Type this 3 times
```python
student = {}
student["name"] = "Bob"
student["grade"] = 85
student["subject"] = "Math"
print(student)
print(student["name"])
```

**Practice Exercise 1.2:** Count character frequencies
```python
word = "hello"
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
```

**Practice Exercise 1.3:** Using get() method (cleaner)
```python
word = "programming"
char_count = {}
for char in word:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
```

**Practice Exercise 1.4:** Dictionary comprehension
```python
numbers = [1, 2, 3, 4, 5]
squared = {num: num * num for num in numbers}
print(squared)
```

**LeetCode Pattern:** Two Sum (Easy)
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Mastery Check:** Can you solve "Two Sum" without looking? Can you explain why dictionary lookup is O(1)? If yes, move to Step 2.

---

### STEP 2: Sets - Fast Membership Testing

#### Why Sets Matter
Sets provide O(1) average time for membership testing. Perfect for "have I seen this before?" problems.

#### Basic Set Operations
```python
# Creating sets
my_set = set()
my_set = {1, 2, 3}
my_set = set([1, 2, 3])

# Adding
my_set.add(4)
my_set.add(5)

# Removing
my_set.remove(4)  # Raises error if not found
my_set.discard(4)  # Safe, no error if not found

# Membership testing
if 3 in my_set:
    print("Found")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2  # {1, 2, 3, 4, 5}
intersection = set1 & set2  # {3}
difference = set1 - set2  # {1, 2}
```

#### Time Complexity
- Add: O(1) average
- Remove: O(1) average
- Membership: O(1) average
- Union/Intersection: O(n + m)

**Practice Exercise 2.1:** Type this 3 times
```python
seen = set()
seen.add(1)
seen.add(2)
seen.add(1)  # Duplicate, won't add
print(seen)
print(1 in seen)
```

**Practice Exercise 2.2:** Find duplicates
```python
numbers = [1, 2, 3, 2, 4, 3, 5]
seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
print(duplicates)
```

**Practice Exercise 2.3:** Remove duplicates from list
```python
numbers = [1, 2, 2, 3, 3, 4, 5]
unique = list(set(numbers))
print(unique)
```

**Practice Exercise 2.4:** Set comprehension
```python
numbers = [1, 2, 3, 4, 5]
squares = {num * num for num in numbers}
print(squares)
```

**LeetCode Pattern:** Contains Duplicate (Easy)
```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Mastery Check:** Can you solve "Contains Duplicate" without looking? Can you explain when to use set vs list? If yes, move to Step 3.

---

### STEP 3: Tuples - Immutable Sequences

#### Why Tuples Matter
Tuples are immutable (can't change), making them hashable. Use them as dictionary keys or when you need ordered, unchangeable data.

#### Basic Tuple Operations
```python
# Creating tuples
my_tuple = (1, 2, 3)
my_tuple = tuple([1, 2, 3])
single = (1,)  # Note the comma!

# Accessing
first = my_tuple[0]
last = my_tuple[-1]

# Unpacking
a, b, c = my_tuple

# Cannot modify (immutable)
# my_tuple[0] = 5  # ERROR!
```

**Practice Exercise 3.1:** Type this 3 times
```python
point = (3, 4)
x, y = point
print(x, y)
```

**Practice Exercise 3.2:** Using tuples as dictionary keys
```python
coordinates = {}
coordinates[(0, 0)] = "origin"
coordinates[(1, 2)] = "point A"
print(coordinates[(0, 0)])
```

**Practice Exercise 3.3:** Returning multiple values
```python
def get_name_age():
    return ("Alice", 25)

name, age = get_name_age()
print(name, age)
```

**LeetCode Pattern:** Using tuples in problems
```python
# Example: Group anagrams by sorted tuple of characters
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

**Mastery Check:** Can you explain when to use tuple vs list? Can you use tuples as dictionary keys? If yes, move to Step 4.

---

### STEP 4: Advanced List Operations

#### List Methods You Must Know
```python
# Adding elements
nums = [1, 2, 3]
nums.append(4)  # Add to end: O(1)
nums.insert(0, 0)  # Insert at index: O(n)
nums.extend([5, 6])  # Add multiple: O(k)

# Removing elements
nums.remove(3)  # Remove first occurrence: O(n)
nums.pop()  # Remove last: O(1)
nums.pop(0)  # Remove at index: O(n)
del nums[0]  # Delete at index: O(n)

# Finding elements
index = nums.index(2)  # Find index: O(n)
count = nums.count(2)  # Count occurrences: O(n)

# Sorting
nums.sort()  # In-place: O(n log n)
sorted_nums = sorted(nums)  # New list: O(n log n)
nums.reverse()  # Reverse: O(n)

# Slicing (CRITICAL for LeetCode)
nums = [0, 1, 2, 3, 4, 5]
nums[1:4]  # [1, 2, 3]
nums[:3]  # [0, 1, 2]
nums[3:]  # [3, 4, 5]
nums[::-1]  # Reverse: [5, 4, 3, 2, 1, 0]
nums[::2]  # Every 2nd: [0, 2, 4]
```

**Practice Exercise 4.1:** Type this 3 times
```python
nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
print(nums)
```

**Practice Exercise 4.2:** List slicing mastery
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:7])
print(nums[:5])
print(nums[5:])
print(nums[::-1])
```

**Practice Exercise 4.3:** List comprehension (Pythonic way)
```python
# Instead of:
squares = []
for i in range(5):
    squares.append(i * i)

# Use:
squares = [i * i for i in range(5)]
print(squares)

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)
```

**Practice Exercise 4.4:** Nested list comprehension
```python
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
```

**LeetCode Pattern:** Reverse array in-place
```python
def reverse_array(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

**Mastery Check:** Can you reverse a list in-place? Can you use list comprehension fluently? If yes, move to Step 5.

---

### STEP 5: Strings - Text Manipulation

#### String Operations for LeetCode
```python
# Basic operations
s = "hello"
s[0]  # 'h'
s[-1]  # 'o'
s[1:4]  # 'ell'
len(s)  # 5

# String methods
s.upper()  # 'HELLO'
s.lower()  # 'hello'
s.strip()  # Remove whitespace
s.split()  # Split into list
s.replace("l", "L")  # 'heLLo'
s.find("e")  # Find index: 1
s.count("l")  # Count: 2

# String building (IMPORTANT!)
# BAD: O(n²) - creates new string each time
result = ""
for char in "hello":
    result += char

# GOOD: O(n) - use list then join
result = []
for char in "hello":
    result.append(char)
result = "".join(result)

# BEST: List comprehension
result = "".join([char for char in "hello"])
```

**Practice Exercise 5.1:** Type this 3 times
```python
s = "Python"
print(s[0])
print(s[-1])
print(s[1:4])
```

**Practice Exercise 5.2:** String building efficiently
```python
words = ["Hello", "World", "Python"]
result = " ".join(words)
print(result)
```

**Practice Exercise 5.3:** String manipulation
```python
s = "  hello world  "
s = s.strip()
s = s.replace(" ", "-")
print(s)
```

**Practice Exercise 5.4:** Check palindrome
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("race car"))
```

**LeetCode Pattern:** Reverse words in string
```python
def reverse_words(s):
    words = s.split()
    return " ".join(words[::-1])
```

**Mastery Check:** Can you reverse a string? Can you build strings efficiently? If yes, move to Step 6.

---

### STEP 6: Collections Module - Advanced Data Structures

#### deque - Double-Ended Queue
```python
from collections import deque

# Creating
dq = deque([1, 2, 3])

# O(1) operations on both ends
dq.append(4)  # Add to right: O(1)
dq.appendleft(0)  # Add to left: O(1)
dq.pop()  # Remove from right: O(1)
dq.popleft()  # Remove from left: O(1)

# Perfect for sliding window problems
```

**Practice Exercise 6.1:** Type this 3 times
```python
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
```

#### defaultdict - Dictionary with Default Values
```python
from collections import defaultdict

# No need to check if key exists
dd = defaultdict(int)
dd["a"] += 1  # Automatically creates key with 0
dd["b"] += 1
print(dd)

# With list as default
dd_list = defaultdict(list)
dd_list["group"].append(1)
dd_list["group"].append(2)
print(dd_list)
```

**Practice Exercise 6.2:** Type this 3 times
```python
from collections import defaultdict
counts = defaultdict(int)
words = ["hello", "world", "hello"]
for word in words:
    counts[word] += 1
print(counts)
```

#### Counter - Count Elements
```python
from collections import Counter

# Count elements automatically
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter)  # Counter({3: 3, 2: 2, 1: 1})
print(counter.most_common(2))  # [(3, 3), (2, 2)]

# Works with strings too
word = "hello"
char_count = Counter(word)
print(char_count)
```

**Practice Exercise 6.3:** Type this 3 times
```python
from collections import Counter
nums = [1, 1, 2, 2, 2, 3]
counter = Counter(nums)
print(counter.most_common(1))
```

**LeetCode Pattern:** Top K Frequent Elements
```python
from collections import Counter

def top_k_frequent(nums, k):
    counter = Counter(nums)
    return [num for num, count in counter.most_common(k)]
```

**Mastery Check:** Can you use deque, defaultdict, and Counter fluently? If yes, move to Part 2.

---

## PART 2: ALGORITHMS & TIME COMPLEXITY

### STEP 7: Time & Space Complexity - Think Like an Interviewer

#### Big O Notation Basics
```python
# O(1) - Constant time
def get_first(arr):
    return arr[0]  # Always takes same time

# O(n) - Linear time
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # Loop through all n elements
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic time
def print_pairs(arr):
    for i in arr:  # n iterations
        for j in arr:  # n iterations each time
            print(i, j)  # Total: n * n = n²

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
```

#### Common Time Complexities
- O(1): Dictionary lookup, array access
- O(log n): Binary search, balanced tree operations
- O(n): Single loop through array
- O(n log n): Sorting, divide-and-conquer
- O(n²): Nested loops
- O(2^n): Recursive algorithms (Fibonacci naive)

**Practice Exercise 7.1:** Identify time complexity
```python
# What's the time complexity?
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
```

**Practice Exercise 7.2:** Optimize this code
```python
# O(n²) version - optimize to O(n)
def find_duplicate_slow(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

# Your optimized O(n) version:
def find_duplicate_fast(arr):
    # Your code here
    pass
```

**Mastery Check:** Can you identify time complexity of code? Can you optimize O(n²) to O(n)? If yes, move to Step 8.

---

### STEP 8: Two Pointers Technique

#### Why Two Pointers?
Perfect for sorted arrays, palindromes, and problems where you need to compare elements from both ends.

#### Pattern 1: Opposite Ends
```python
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
```

**Practice Exercise 8.1:** Type this 3 times
```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

**Practice Exercise 8.2:** Remove duplicates from sorted array
```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

#### Pattern 2: Fast & Slow Pointers
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Practice Exercise 8.3:** Find middle of array
```python
def find_middle(nums):
    slow = fast = 0
    while fast < len(nums) and fast + 1 < len(nums):
        slow += 1
        fast += 2
    return nums[slow]
```

**LeetCode Problems to Solve:**
1. Two Sum II (Easy)
2. Valid Palindrome (Easy)
3. Remove Duplicates from Sorted Array (Easy)
4. Container With Most Water (Medium)

**Mastery Check:** Can you solve "Two Sum II" using two pointers? Can you explain when to use this technique? If yes, move to Step 9.

---

### STEP 9: Sliding Window Technique

#### Why Sliding Window?
Perfect for subarray/substring problems with fixed or variable window size.

#### Pattern 1: Fixed Window Size
```python
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
```

**Practice Exercise 9.1:** Type this 3 times
```python
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
```

#### Pattern 2: Variable Window Size
```python
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
```

**Practice Exercise 9.2:** Minimum window substring pattern
```python
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
```

**LeetCode Problems to Solve:**
1. Maximum Average Subarray I (Easy)
2. Longest Substring Without Repeating Characters (Medium)
3. Minimum Window Substring (Hard)
4. Sliding Window Maximum (Hard)

**Mastery Check:** Can you solve "Longest Substring Without Repeating Characters"? Can you explain fixed vs variable window? If yes, move to Step 10.

---

### STEP 10: Hash Map Patterns

#### Pattern 1: Frequency Counting
```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

**Practice Exercise 10.1:** Type this 3 times
```python
def find_anagram_mappings(nums1, nums2):
    mapping = {}
    for i, num in enumerate(nums2):
        mapping[num] = i
    
    result = []
    for num in nums1:
        result.append(mapping[num])
    return result
```

#### Pattern 2: Prefix Sum with Hash Map
```python
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
```

**Practice Exercise 10.2:** Type this 3 times
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**LeetCode Problems to Solve:**
1. Group Anagrams (Medium)
2. Subarray Sum Equals K (Medium)
3. Two Sum (Easy)
4. Longest Consecutive Sequence (Medium)

**Mastery Check:** Can you solve "Subarray Sum Equals K"? Can you explain prefix sum technique? If yes, move to Step 11.

---

### STEP 11: Sorting & Searching

#### Built-in Sorting
```python
# Sort in-place
nums = [3, 1, 4, 1, 5]
nums.sort()  # [1, 1, 3, 4, 5]
nums.sort(reverse=True)  # [5, 4, 3, 1, 1]

# Sort with custom key
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
students.sort(key=lambda x: x[1])  # Sort by age

# Create new sorted list
sorted_nums = sorted(nums)
```

**Practice Exercise 11.1:** Type this 3 times
```python
nums = [64, 34, 25, 12, 22, 11, 90]
nums.sort()
print(nums)
```

#### Binary Search Template
```python
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
```

**Practice Exercise 11.2:** Type this 3 times
```python
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
```

#### Finding Boundaries
```python
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
```

**LeetCode Problems to Solve:**
1. Binary Search (Easy)
2. Search Insert Position (Easy)
3. Find First and Last Position (Medium)
4. Search in Rotated Sorted Array (Medium)

**Mastery Check:** Can you implement binary search from memory? Can you find insertion point? If yes, move to Step 12.

---

### STEP 12: Stack & Queue Patterns

#### Stack - LIFO (Last In First Out)
```python
# Using list as stack
stack = []
stack.append(1)  # Push: O(1)
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop: O(1) - removes and returns last
# top = 3

# Common patterns: parentheses matching, monotonic stack
```

**Practice Exercise 12.1:** Valid parentheses
```python
def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0
```

#### Queue - FIFO (First In First Out)
```python
from collections import deque

# Using deque as queue
queue = deque()
queue.append(1)  # Enqueue: O(1)
queue.append(2)
queue.append(3)
front = queue.popleft()  # Dequeue: O(1) - removes first
# front = 1
```

**Practice Exercise 12.2:** Type this 3 times
```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
while queue:
    print(queue.popleft())
```

#### Monotonic Stack Pattern
```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    
    return result
```

**LeetCode Problems to Solve:**
1. Valid Parentheses (Easy)
2. Daily Temperatures (Medium)
3. Next Greater Element (Medium)
4. Implement Queue using Stacks (Easy)

**Mastery Check:** Can you solve "Valid Parentheses"? Can you explain when to use stack vs queue? If yes, move to Step 13.

---

### STEP 13: Recursion & Backtracking

#### Basic Recursion
```python
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)
```

**Practice Exercise 13.1:** Type this 3 times
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

#### Backtracking Template
```python
def backtrack(candidates, path, result):
    # Base case: solution found
    if is_solution(path):
        result.append(path[:])  # Copy path
        return
    
    # Try all candidates
    for candidate in candidates:
        if is_valid(candidate, path):
            path.append(candidate)  # Make choice
            backtrack(candidates, path, result)
            path.pop()  # Undo choice (backtrack)
```

**Practice Exercise 13.2:** Generate all subsets
```python
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
```

**Practice Exercise 13.3:** Generate permutations
```python
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
```

**LeetCode Problems to Solve:**
1. Subsets (Medium)
2. Permutations (Medium)
3. Combination Sum (Medium)
4. N-Queens (Hard)

**Mastery Check:** Can you generate all subsets recursively? Can you explain backtracking? If yes, move to Step 14.

---

### STEP 14: Dynamic Programming Basics

#### DP Pattern Recognition
DP problems have:
1. Overlapping subproblems
2. Optimal substructure

#### Pattern 1: 1D DP
```python
def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

**Practice Exercise 14.1:** Type this 3 times
```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
```

#### Pattern 2: Space-Optimized DP
```python
def climb_stairs_optimized(n):
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1
```

**Practice Exercise 14.2:** House Robber
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]
```

**LeetCode Problems to Solve:**
1. Climbing Stairs (Easy)
2. House Robber (Easy)
3. Best Time to Buy and Sell Stock (Easy)
4. Coin Change (Medium)

**Mastery Check:** Can you solve "Climbing Stairs" with DP? Can you optimize space? If yes, move to Step 15.

---

### STEP 15: Tree & Graph Basics

#### Binary Tree Traversal
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In-order: Left -> Root -> Right
def inorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    dfs(root)
    return result

# Pre-order: Root -> Left -> Right
def preorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

# Post-order: Left -> Right -> Root
def postorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
    dfs(root)
    return result
```

**Practice Exercise 15.1:** Type this 3 times
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

#### BFS (Breadth-First Search)
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

**Practice Exercise 15.2:** Type this 3 times
```python
from collections import deque

def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

**LeetCode Problems to Solve:**
1. Maximum Depth of Binary Tree (Easy)
2. Same Tree (Easy)
3. Binary Tree Level Order Traversal (Medium)
4. Validate Binary Search Tree (Medium)

**Mastery Check:** Can you traverse a tree? Can you implement BFS? If yes, move to Part 3.

---

## PART 3: LEETCODE PATTERNS & STRATEGIES

### STEP 16: Problem-Solving Framework

#### The 5-Step Process
1. **Understand:** Read problem carefully, identify constraints
2. **Examples:** Work through examples manually
3. **Approach:** Think of brute force first, then optimize
4. **Code:** Implement solution
5. **Test:** Test with edge cases

#### Template for Every Problem
```python
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
        pass
    
    # Step 4: Return result
    return result
```

**Practice Exercise 16.1:** Solve this problem using the framework
```python
# Problem: Find all numbers that appear twice in array
# Input: [4,3,2,7,8,2,3,1]
# Output: [2,3]

def find_duplicates(nums):
    # Your solution here
    pass
```

---

### STEP 17: Common LeetCode Patterns Cheat Sheet

#### Pattern 1: Two Pointers
- **When:** Sorted array, palindrome, comparing ends
- **Time:** O(n)
- **Example:** Two Sum II, Valid Palindrome

#### Pattern 2: Sliding Window
- **When:** Subarray/substring problems
- **Time:** O(n)
- **Example:** Longest Substring, Minimum Window

#### Pattern 3: Hash Map
- **When:** Need O(1) lookup, frequency counting
- **Time:** O(n)
- **Example:** Two Sum, Group Anagrams

#### Pattern 4: Stack
- **When:** LIFO needed, matching pairs, monotonic
- **Time:** O(n)
- **Example:** Valid Parentheses, Daily Temperatures

#### Pattern 5: Binary Search
- **When:** Sorted array, search space reduction
- **Time:** O(log n)
- **Example:** Binary Search, Search Insert Position

#### Pattern 6: DFS/BFS
- **When:** Tree/Graph traversal, path finding
- **Time:** O(V + E)
- **Example:** Tree Traversal, Word Ladder

#### Pattern 7: Dynamic Programming
- **When:** Overlapping subproblems, optimization
- **Time:** Usually O(n²) or O(n)
- **Example:** Climbing Stairs, Coin Change

#### Pattern 8: Backtracking
- **When:** Generate all solutions, constraint satisfaction
- **Time:** Usually exponential
- **Example:** Subsets, Permutations

---

### STEP 18: Python-Specific Optimizations

#### List vs Set vs Dict Lookup
```python
# O(n) - List
if item in my_list:
    pass

# O(1) - Set/Dict
if item in my_set:
    pass
if key in my_dict:
    pass
```

#### String Building
```python
# O(n²) - BAD
result = ""
for char in string:
    result += char

# O(n) - GOOD
result = []
for char in string:
    result.append(char)
result = "".join(result)

# O(n) - BEST
result = "".join([char for char in string])
```

#### List Comprehension vs Loop
```python
# More Pythonic and often faster
squares = [x * x for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

---

## FINAL MASTERY CHECKLIST

Before tackling LeetCode problems, ensure you can:

### Data Structures
- [ ] Use dictionaries fluently (get, items, keys, values)
- [ ] Use sets for O(1) membership testing
- [ ] Use tuples as dictionary keys
- [ ] Master list slicing and comprehension
- [ ] Use collections.deque, defaultdict, Counter
- [ ] Build strings efficiently

### Algorithms
- [ ] Identify time/space complexity
- [ ] Implement two pointers
- [ ] Implement sliding window (fixed & variable)
- [ ] Use hash maps for frequency counting
- [ ] Implement binary search
- [ ] Use stack/queue appropriately
- [ ] Write recursive functions
- [ ] Implement basic DP patterns
- [ ] Traverse trees (DFS/BFS)

### Problem-Solving
- [ ] Follow 5-step problem-solving framework
- [ ] Identify which pattern to use
- [ ] Handle edge cases
- [ ] Optimize from brute force
- [ ] Test with examples

---

## RECOMMENDED LEETCODE PROGRESSION

### Easy Problems (Master these first)
1. Two Sum
2. Contains Duplicate
3. Valid Anagram
4. Valid Parentheses
5. Best Time to Buy and Sell Stock
6. Maximum Subarray
7. Climbing Stairs
8. House Robber
9. Reverse Linked List
10. Merge Two Sorted Lists

### Medium Problems (After mastering Easy)
1. Two Sum II
2. Longest Substring Without Repeating Characters
3. Group Anagrams
4. Top K Frequent Elements
5. Product of Array Except Self
6. Longest Palindromic Substring
7. Container With Most Water
8. 3Sum
9. Binary Tree Level Order Traversal
10. Coin Change

### Hard Problems (After mastering Medium)
1. Trapping Rain Water
2. Merge k Sorted Lists
3. Serialize and Deserialize Binary Tree
4. Word Ladder II
5. N-Queens

---

## INTERVIEW TIPS

1. **Clarify:** Ask questions about input/output, constraints
2. **Examples:** Work through examples out loud
3. **Think Aloud:** Explain your thought process
4. **Start Simple:** Begin with brute force, then optimize
5. **Test:** Always test with edge cases
6. **Time Management:** 5 min understand, 10 min think, 20 min code, 5 min test

---

## DAILY PRACTICE ROUTINE

**Week 1-2:** Master data structures (Steps 1-6)
- Practice each concept 3-4 times
- Solve 2-3 easy problems per day

**Week 3-4:** Master algorithms (Steps 7-15)
- Implement each pattern from scratch
- Solve 3-5 easy/medium problems per day

**Week 5-6:** Pattern recognition (Steps 16-18)
- Focus on identifying patterns
- Solve 5-7 problems per day
- Review solutions and optimize

**Week 7+:** Interview prep
- Mock interviews
- Focus on medium problems
- Time yourself (45 min per problem)

---

**Remember:** Mastery comes from consistent practice. Type every solution yourself. Understand WHY each approach works. You've got this! 🚀


