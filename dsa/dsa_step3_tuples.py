# DSA STEP 3 PRACTICE: Tuples
# Type each exercise 3-4 times until it's muscle memory

# Exercise 3.1: Basic tuple operations
point = (3, 4)
x, y = point
print(x, y)

# Exercise 3.2: Using tuples as dictionary keys
coordinates = {}
coordinates[(0, 0)] = "origin"
coordinates[(1, 2)] = "point A"
print(coordinates[(0, 0)])

# Exercise 3.3: Returning multiple values
def get_name_age():
    return ("Alice", 25)

name, age = get_name_age()
print(name, age)

# Exercise 3.4: Tuple unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")

# LeetCode Pattern: Group Anagrams using tuples
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())

# Test it
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


