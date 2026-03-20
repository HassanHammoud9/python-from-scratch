# DSA STEP 12 PRACTICE: Stack & Queue Patterns
# Type each exercise 3-4 times until it's muscle memory

from collections import deque

# Stack - LIFO (Last In First Out)
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - removes and returns last
print(f"Stack: {stack}, Popped: {top}")

# Exercise 12.1: Valid Parentheses
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

# Queue - FIFO (First In First Out)
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
front = queue.popleft()  # Dequeue - removes first
print(f"Queue: {list(queue)}, Dequeued: {front}")

# Exercise 12.2: Queue operations
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
while queue:
    print(queue.popleft())

# Monotonic Stack Pattern
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    
    return result

# Exercise 12.3: Daily Temperatures
def daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    
    return result

# Exercise 12.4: Implement Queue using Stacks
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self, x):
        self.stack1.append(x)
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2

# Test
print(is_valid("()[]{}"))
print(is_valid("([)]"))
print(next_greater_element([4, 5, 2, 10]))
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))


