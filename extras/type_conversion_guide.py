# TYPE CONVERSION GUIDE: When to Convert Variables
# This explains when and why you need to convert between int, float, and str

# ============================================
# THE GOLDEN RULE:
# ============================================
# input() ALWAYS returns a STRING (text), even if user types a number!
# If you want to do MATH, you MUST convert to int() or float()
# If you want to PRINT numbers with text, you MUST convert to str()

# ============================================
# WHEN TO USE int() - Whole Numbers
# ============================================
# Use int() when:
# 1. User inputs a number and you need to do math (addition, subtraction, etc.)
# 2. You're working with whole numbers (no decimals)
# 3. Examples: age, count, number of items, etc.

# Example 1: User enters age - need to calculate something
age = input("Enter your age: ")  # This is a STRING like "25"
age_number = int(age)  # Convert to NUMBER: 25
next_year = age_number + 1  # Now we can do math!
print("Next year you'll be " + str(next_year))  # Convert back to string for printing

# Example 2: Counting items
items = input("How many items? ")  # String: "5"
item_count = int(items)  # Number: 5
total = item_count * 10  # Math works!
print("Total cost: " + str(total))

# ============================================
# WHEN TO USE float() - Decimal Numbers
# ============================================
# Use float() when:
# 1. User inputs a number with decimals (or might have decimals)
# 2. You're doing calculations that might result in decimals
# 3. Examples: money, measurements, percentages, averages, etc.

# Example 1: Money calculations
price = input("Enter price: ")  # String: "19.99"
price_num = float(price)  # Number: 19.99
tax = price_num * 0.08  # Calculate tax (results in decimal)
print("Tax: " + str(tax))

# Example 2: Measurements
radius = input("Enter radius: ")  # String: "5.5"
radius_num = float(radius)  # Number: 5.5
area = 3.14 * radius_num * radius_num  # Math with decimals
print("Area: " + str(area))

# Example 3: Averages (always use float!)
num1 = input("First number: ")
num2 = input("Second number: ")
average = (float(num1) + float(num2)) / 2  # Division often gives decimals
print("Average: " + str(average))

# ============================================
# WHEN TO USE str() - Converting Numbers to Text
# ============================================
# Use str() when:
# 1. You have a number and want to combine it with text using +
# 2. You want to print numbers along with text
# 3. You're building a message that includes numbers

# Example 1: Combining number with text
age = 25
# WRONG: print("I am " + age + " years old")  # ERROR! Can't add string + number
# RIGHT:
print("I am " + str(age) + " years old")  # Convert number to string first

# Example 2: Building a message
score = 95
message = "Your score is " + str(score) + " points"
print(message)

# ============================================
# COMMON MISTAKES & SOLUTIONS
# ============================================

# MISTAKE 1: Trying to do math with strings
# WRONG:
num1 = input("Enter number: ")  # "5" (string)
num2 = input("Enter number: ")  # "3" (string)
# result = num1 + num2  # This gives "53" (concatenation), not 8!

# RIGHT:
num1 = input("Enter number: ")
num2 = input("Enter number: ")
result = int(num1) + int(num2)  # Convert first, then add
print(result)  # 8

# MISTAKE 2: Trying to combine number with string
# WRONG:
age = 20
# print("I am " + age)  # ERROR! Can't add string + int

# RIGHT:
age = 20
print("I am " + str(age))  # Convert to string first

# MISTAKE 3: Using int() when you need float()
# WRONG:
price = input("Enter price: ")  # User types "19.99"
price_num = int(price)  # This gives 19 (loses decimal part!)

# RIGHT:
price = input("Enter price: ")
price_num = float(price)  # This gives 19.99 (keeps decimals)

# ============================================
# QUICK DECISION GUIDE
# ============================================

# Q: User inputs something, I want to do math?
# A: Convert with int() or float()
#    - Use int() for whole numbers (age, count, items)
#    - Use float() for decimals (money, measurements, averages)

# Q: I have a number, I want to print it with text?
# A: Convert with str() before combining

# Q: User inputs text, I just want to display it?
# A: No conversion needed! input() already gives you a string

# Q: I'm doing division?
# A: Usually use float() - division often gives decimals
#    Example: 5 / 2 = 2.5 (not 2!)

# ============================================
# PRACTICE EXAMPLES
# ============================================

# Example 1: Age calculator
birth_year = input("Enter birth year: ")  # String
current_year = input("Enter current year: ")  # String
age = int(current_year) - int(birth_year)  # Convert to do math
print("You are " + str(age) + " years old")  # Convert to print

# Example 2: Shopping calculator
item_price = input("Enter item price: ")  # String: "12.50"
quantity = input("Enter quantity: ")  # String: "3"
total = float(item_price) * int(quantity)  # Convert both, then multiply
print("Total: $" + str(total))  # Convert to print

# Example 3: Temperature converter
celsius = input("Enter temperature in Celsius: ")  # String: "25.5"
fahrenheit = (float(celsius) * 9/5) + 32  # Convert to do math
print(celsius + "°C is " + str(fahrenheit) + "°F")  # Convert result to print

# ============================================
# SUMMARY TABLE
# ============================================
# From          To          When to Use
# -------------------------------------------
# input()      int()       User enters whole number, need math
# input()      float()     User enters decimal, need math
# number       str()       Need to combine number with text
# string       int()       String contains number, need math
# string       float()     String contains decimal, need math

# ============================================
# REMEMBER:
# ============================================
# 1. input() = always string (text)
# 2. Math operations = need int() or float()
# 3. Printing numbers with text = need str()
# 4. When in doubt, use float() - it works for whole numbers too!
