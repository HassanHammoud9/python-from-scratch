# INT AND FLOAT: Can You Mix Them?
# Short answer: YES! Python automatically converts int to float when needed

# ============================================
# THE RULE: int + float = float
# ============================================
# Python automatically converts int to float when you mix them
# The result is always a float

# Example 1: Adding int and float
num1 = 5      # int
num2 = 3.5    # float
result = num1 + num2  # Python converts 5 to 5.0, then adds
print(result)  # 8.5 (float)
print(type(result))  # <class 'float'>

# Example 2: Multiplying int and float
whole = 10    # int
decimal = 2.5  # float
product = whole * decimal
print(product)  # 25.0 (float)

# Example 3: Division always gives float
result1 = 10 / 2   # Even dividing two ints!
print(result1)     # 5.0 (float, not int!)
print(type(result1))  # <class 'float'>

result2 = 7 / 3
print(result2)  # 2.3333333333333335 (float)

# ============================================
# WHAT CAN'T YOU MIX?
# ============================================
# You CANNOT mix STRING with NUMBER (int or float)

# This works (int + float):
print(5 + 3.5)  # 8.5 ✅

# This DOESN'T work (string + number):
# print("5" + 3.5)  # ERROR! ❌
# print("5" + 5)    # ERROR! ❌

# To fix, convert string to number first:
print(float("5") + 3.5)  # 8.5 ✅
print(int("5") + 3.5)    # 8.5 ✅ (int becomes float)

# ============================================
# PRACTICAL EXAMPLES
# ============================================

# Example 1: User inputs mixed types
age = int(input("Enter age: "))      # User types: 25 (becomes int)
height = float(input("Enter height: "))  # User types: 5.9 (becomes float)
# You can add them!
total = age + height  # Works! Result is float
print(total)  # 30.9

# Example 2: Calculations with mixed types
items = 5        # int
price = 2.99     # float
total_cost = items * price  # Works! Result is float
print(total_cost)  # 14.95

# Example 3: Even if you start with int, division makes it float
whole_number = 10
half = whole_number / 2  # Division always gives float
print(half)  # 5.0 (not 5!)

# ============================================
# WHEN DO YOU NEED TO WORRY?
# ============================================
# You ONLY need to convert when:
# 1. STRING + NUMBER (need to convert string first)
# 2. NUMBER + STRING for printing (need to convert number to string)

# Example: String + Number = ERROR
age_str = "25"  # string
age_num = 5     # int
# result = age_str + age_num  # ERROR! Can't add string + int

# Fix: Convert string to number
result = int(age_str) + age_num  # Works! 30

# Example: Number + String for printing = ERROR
age = 25
# print("I am " + age)  # ERROR! Can't add string + int

# Fix: Convert number to string
print("I am " + str(age))  # Works!

# ============================================
# SUMMARY TABLE
# ============================================
# Operation        Result        Works?
# -------------------------------------------
# int + int        int           ✅ Yes
# int + float      float         ✅ Yes (auto-converts)
# float + float    float         ✅ Yes
# string + int     ERROR         ❌ No (need conversion)
# string + float   ERROR         ❌ No (need conversion)
# int / int        float         ✅ Yes (division always gives float)

# ============================================
# KEY TAKEAWAYS
# ============================================
# 1. ✅ int + float = WORKS (Python auto-converts)
# 2. ✅ int / int = float (division always gives float)
# 3. ❌ string + number = ERROR (need to convert)
# 4. ❌ number + string = ERROR (need str() to print)

# ============================================
# PRACTICE EXAMPLES
# ============================================

# Practice 1: Mix int and float
a = 10
b = 3.5
print(a + b)      # 13.5
print(a * b)      # 35.0
print(a - b)      # 6.5

# Practice 2: Division always gives float
print(10 / 2)     # 5.0 (not 5!)
print(7 / 3)       # 2.3333333333333335

# Practice 3: What happens with user input?
# (Uncomment to test)
# num1 = int(input("Enter whole number: "))    # User: 5
# num2 = float(input("Enter decimal: "))       # User: 2.5
# print(num1 + num2)  # 7.5 (works perfectly!)

# Practice 4: The only problem is STRING + NUMBER
age_text = "25"
age_number = 5
# print(age_text + age_number)  # ERROR!
print(int(age_text) + age_number)  # Works! 30
