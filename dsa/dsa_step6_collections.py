# DSA STEP 6 PRACTICE: Collections Module
# Type each exercise 3-4 times until it's muscle memory

from collections import deque, defaultdict, Counter

# Exercise 6.1: deque - Double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
print(dq.popleft())
print(dq.pop())

# Exercise 6.2: defaultdict - Dictionary with default values
counts = defaultdict(int)
words = ["hello", "world", "hello"]
for word in words:
    counts[word] += 1
print(counts)

# defaultdict with list
dd_list = defaultdict(list)
dd_list["group"].append(1)
dd_list["group"].append(2)
print(dd_list)

# Exercise 6.3: Counter - Count elements automatically
nums = [1, 2, 2, 3, 3, 3]
counter = Counter(nums)
print(counter)
print(counter.most_common(2))

# Counter with strings
word = "hello"
char_count = Counter(word)
print(char_count)

# LeetCode Pattern: Top K Frequent Elements
def top_k_frequent(nums, k):
    counter = Counter(nums)
    return [num for num, count in counter.most_common(k)]

# Test it
print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]


