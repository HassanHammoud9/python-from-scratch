# DSA STEP 15 PRACTICE: Tree & Graph Basics
# Type each exercise 3-4 times until it's muscle memory

# Binary Tree Node Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In-order Traversal: Left -> Root -> Right
def inorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
    dfs(root)
    return result

# Pre-order Traversal: Root -> Left -> Right
def preorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

# Post-order Traversal: Left -> Right -> Root
def postorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
    dfs(root)
    return result

# Exercise 15.1: Maximum Depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# BFS (Breadth-First Search) - Level Order Traversal
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

# Exercise 15.2: BFS for Graphs
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

# Exercise 15.3: Same Tree
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Exercise 15.4: Validate Binary Search Tree
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# Create a test tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order:", inorder_traversal(root))
print("Pre-order:", preorder_traversal(root))
print("Post-order:", postorder_traversal(root))
print("Max depth:", max_depth(root))
print("Level order:", level_order_traversal(root))

# Test graph BFS
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS:", bfs_graph(graph, 'A'))


