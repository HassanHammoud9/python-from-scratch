# Python Tutorial: Learn by Doing

The goal is simple: get comfortable writing Python without looking at examples.

**How to use this:**
- Read each concept, then type out the examples yourself (don't copy paste)
- Complete every practice exercise
- Repeat each exercise 3 to 4 times until it feels natural
- Only move to the next step when you can write the code from memory

Practice files are in the `basics/` folder. Run them with `python3 basics/stepX_practice.py`.

---

## STEP 1: Your First Python Program

### What is Python?
Python is a programming language that reads like English. You write instructions, and Python executes them.

### Your First Program
Every Python program starts with understanding how to run code.

**Example 1: Print a message**
```python
print("Hello, World!")
```

**What happened?**
- `print()` is a function (a command that does something)
- The text inside quotes `"Hello, World!"` is a string (text data)
- Python executes this and displays the message

**Practice Exercise 1.1:**
Type this 3 times, changing the message each time:
```python
print("My name is [your name]")
print("I am learning Python")
print("This is fun!")
```

**Practice Exercise 1.2:**
Type these variations 3 times each:
```python
print("Python")
print("is")
print("awesome")
```

**Practice Exercise 1.3:**
Try printing numbers (no quotes needed):
```python
print(5)
print(10)
print(100)
```

**Practice Exercise 1.4:**
Mix text and numbers:
```python
print("I have")
print(3)
print("cats")
```

**Mastery Check:** Can you write a program that prints your name, age, and favorite color without looking at examples? If yes, move to Step 2.

---

## STEP 2: Variables - Storing Information

### What is a Variable?
A variable is like a labeled box where you store information. You give it a name and put a value inside.

### Basic Variable Syntax
```python
variable_name = value
```

**Example 2.1: Storing text**
```python
name = "Alice"
print(name)
```

**What happened?**
- `name` is the variable name (the label)
- `"Alice"` is the value stored inside
- `print(name)` displays what's stored in `name`

**Example 2.2: Storing numbers**
```python
age = 25
print(age)
```

**Example 2.3: Using variables**
```python
name = "Bob"
age = 30
print(name)
print(age)
```

**Practice Exercise 2.1:**
Type this 3 times, changing the values:
```python
my_name = "Your Name"
my_age = 20
print(my_name)
print(my_age)
```

**Practice Exercise 2.2:**
Create variables for your favorite things:
```python
favorite_color = "blue"
favorite_food = "pizza"
favorite_number = 7
print(favorite_color)
print(favorite_food)
print(favorite_number)
```

**Practice Exercise 2.3:**
Change variable values:
```python
x = 5
print(x)
x = 10
print(x)
x = 15
print(x)
```

**Practice Exercise 2.4:**
Combine variables with print:
```python
name = "Charlie"
print("Hello, my name is")
print(name)
```

**Mastery Check:** Can you create 5 different variables and print them all without looking? If yes, move to Step 3.

---

## STEP 3: Combining Text - String Concatenation

### What is Concatenation?
Concatenation means joining strings together. Use `+` to combine text.

**Example 3.1: Basic concatenation**
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + last_name
print(full_name)
```

**Example 3.2: Adding spaces**
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
```

**Example 3.3: Multiple concatenations**
```python
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)
```

**Practice Exercise 3.1:**
Type this 3 times with different names:
```python
first = "Jane"
last = "Smith"
full = first + " " + last
print(full)
```

**Practice Exercise 3.2:**
Create a sentence:
```python
subject = "Python"
verb = "is"
adjective = "awesome"
sentence = subject + " " + verb + " " + adjective
print(sentence)
```

**Practice Exercise 3.3:**
Build a greeting:
```python
hello = "Hello"
name = "Bob"
exclamation = "!"
greeting = hello + ", " + name + exclamation
print(greeting)
```

**Practice Exercise 3.4:**
Combine multiple variables:
```python
part1 = "I"
part2 = "love"
part3 = "coding"
part4 = "in"
part5 = "Python"
sentence = part1 + " " + part2 + " " + part3 + " " + part4 + " " + part5
print(sentence)
```

**Mastery Check:** Can you create a program that combines 4 variables into one sentence without looking? If yes, move to Step 4.

---

## STEP 4: Numbers and Math Operations

### Basic Math Operations
Python can do math! Use these operators:
- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

**Example 4.1: Simple calculations**
```python
result = 5 + 3
print(result)
```

**Example 4.2: Multiple operations**
```python
sum_result = 10 + 5
difference = 10 - 5
product = 10 * 5
quotient = 10 / 5
print(sum_result)
print(difference)
print(product)
print(quotient)
```

**Example 4.3: Using variables**
```python
a = 10
b = 3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
print(addition)
print(subtraction)
print(multiplication)
print(division)
```

**Practice Exercise 4.1:**
Type these calculations 3 times each:
```python
result1 = 7 + 8
result2 = 15 - 6
result3 = 4 * 5
result4 = 20 / 4
print(result1)
print(result2)
print(result3)
print(result4)
```

**Practice Exercise 4.2:**
Create variables and calculate:
```python
x = 12
y = 4
add = x + y
subtract = x - y
multiply = x * y
divide = x / y
print(add)
print(subtract)
print(multiply)
print(divide)
```

**Practice Exercise 4.3:**
Calculate area of a rectangle:
```python
length = 10
width = 5
area = length * width
print(area)
```

**Practice Exercise 4.4:**
Calculate total cost:
```python
item1_price = 15
item2_price = 20
item3_price = 10
total = item1_price + item2_price + item3_price
print(total)
```

**Mastery Check:** Can you write a program that calculates the sum, difference, product, and quotient of two numbers without looking? If yes, move to Step 5.

---

## STEP 5: Getting Input from User

### What is Input?
Input lets your program ask the user for information while it's running.

**Example 5.1: Getting text input**
```python
name = input("What is your name? ")
print("Hello, " + name)
```

**What happened?**
- `input()` pauses the program and waits for user to type
- The text inside quotes is the question shown to the user
- Whatever the user types gets stored in the variable

**Example 5.2: Getting number input**
```python
age = input("How old are you? ")
print("You are " + age + " years old")
```

**Example 5.3: Multiple inputs**
```python
name = input("What is your name? ")
age = input("How old are you? ")
print("Hello, " + name + ". You are " + age + " years old.")
```

**Practice Exercise 5.1:**
Type this 3 times, run it, and try different inputs:
```python
name = input("Enter your name: ")
print("Nice to meet you, " + name)
```

**Practice Exercise 5.2:**
Ask for favorite color:
```python
color = input("What is your favorite color? ")
print("I like " + color + " too!")
```

**Practice Exercise 5.3:**
Ask multiple questions:
```python
first = input("What is your first name? ")
last = input("What is your last name? ")
print("Your full name is " + first + " " + last)
```

**Practice Exercise 5.4:**
Create a simple survey:
```python
name = input("What is your name? ")
food = input("What is your favorite food? ")
hobby = input("What is your hobby? ")
print(name + " likes " + food + " and enjoys " + hobby)
```

**Mastery Check:** Can you write a program that asks 3 questions and combines the answers into one sentence? If yes, move to Step 6.

---

## STEP 6: Converting Input to Numbers

### Why Convert?
When you use `input()`, Python treats everything as text. To do math, you need to convert to numbers.

**Example 6.1: Converting to integer**
```python
age = input("How old are you? ")
age_number = int(age)
next_year = age_number + 1
print("Next year you will be " + str(next_year))
```

**What happened?**
- `int()` converts text to a whole number (integer)
- `str()` converts a number back to text for printing

**Example 6.2: Math with converted input**
```python
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) + int(num2)
print("The sum is " + str(result))
```

**Example 6.3: Using float for decimals**
```python
price = input("Enter price: ")
price_number = float(price)
tax = price_number * 0.1
total = price_number + tax
print("Total with tax: " + str(total))
```

**Practice Exercise 6.1:**
Type this 3 times:
```python
num = input("Enter a number: ")
doubled = int(num) * 2
print("Double is " + str(doubled))
```

**Practice Exercise 6.2:**
Calculate sum of two numbers:
```python
a = input("First number: ")
b = input("Second number: ")
sum_result = int(a) + int(b)
print("Sum: " + str(sum_result))
```

**Practice Exercise 6.3:**
Calculate area of a circle (radius squared times 3.14):
```python
radius = input("Enter radius: ")
area = float(radius) * float(radius) * 3.14
print("Area is " + str(area))
```

**Practice Exercise 6.4:**
Calculate total with tip:
```python
bill = input("Enter bill amount: ")
tip_percent = input("Enter tip percent: ")
bill_num = float(bill)
tip_num = float(tip_percent)
tip_amount = bill_num * (tip_num / 100)
total = bill_num + tip_amount
print("Total: " + str(total))
```

**Mastery Check:** Can you write a program that asks for two numbers, multiplies them, and prints the result? If yes, move to Step 7.

---

## STEP 7: Making Decisions - If Statements

### What is an If Statement?
An if statement lets your program make decisions based on conditions.

**Example 7.1: Simple if**
```python
age = 20
if age >= 18:
    print("You are an adult")
```

**What happened?**
- `if` checks a condition
- `age >= 18` means "age is greater than or equal to 18"
- The code indented under `if` only runs if the condition is True
- **Important:** Python uses indentation (spaces) to show what code belongs together

**Example 7.2: If with else**
```python
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Example 7.3: Multiple conditions**
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**Practice Exercise 7.1:**
Type this 3 times with different values:
```python
temperature = 75
if temperature > 70:
    print("It's warm")
else:
    print("It's cold")
```

**Practice Exercise 7.2:**
Check if number is positive:
```python
number = 5
if number > 0:
    print("Positive")
else:
    print("Negative or zero")
```

**Practice Exercise 7.3:**
Age checker:
```python
age = input("How old are you? ")
age_num = int(age)
if age_num >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")
```

**Practice Exercise 7.4:**
Grade calculator:
```python
score = input("Enter your score: ")
score_num = int(score)
if score_num >= 90:
    print("Excellent!")
elif score_num >= 80:
    print("Good job!")
elif score_num >= 70:
    print("Not bad")
else:
    print("Keep practicing")
```

**Mastery Check:** Can you write a program that asks for a number and tells if it's even or odd? (Hint: use `%` for remainder, `number % 2 == 0` means even) If yes, move to Step 8.

---

## STEP 8: Repeating Actions - Loops

### What is a Loop?
A loop repeats code multiple times. Two main types: `for` and `while`.

**Example 8.1: For loop with range**
```python
for i in range(5):
    print("Hello")
```

**What happened?**
- `for i in range(5)` means "repeat 5 times"
- `i` is a variable that counts (0, 1, 2, 3, 4)
- The indented code runs each time

**Example 8.2: Counting with for loop**
```python
for i in range(5):
    print(i)
```

**Example 8.3: While loop**
```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

**Practice Exercise 8.1:**
Type this 3 times:
```python
for i in range(3):
    print("Python")
```

**Practice Exercise 8.2:**
Count from 1 to 5:
```python
for i in range(1, 6):
    print(i)
```

**Practice Exercise 8.3:**
Print numbers 0 to 9:
```python
for number in range(10):
    print(number)
```

**Practice Exercise 8.4:**
While loop counter:
```python
counter = 0
while counter < 5:
    print("Count: " + str(counter))
    counter = counter + 1
```

**Mastery Check:** Can you write a program that prints numbers from 1 to 10 using a for loop? If yes, move to Step 9.

---

## STEP 9: Lists - Storing Multiple Items

### What is a List?
A list stores multiple items in order. Like a shopping list!

**Example 9.1: Creating a list**
```python
fruits = ["apple", "banana", "orange"]
print(fruits)
```

**Example 9.2: Accessing list items**
```python
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # First item (starts at 0)
print(fruits[1])  # Second item
print(fruits[2])  # Third item
```

**Example 9.3: Adding to a list**
```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)
```

**Practice Exercise 9.1:**
Type this 3 times with different items:
```python
colors = ["red", "blue", "green"]
print(colors)
```

**Practice Exercise 9.2:**
Access specific items:
```python
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[2])
```

**Practice Exercise 9.3:**
Add items to list:
```python
shopping = ["milk"]
shopping.append("bread")
shopping.append("eggs")
print(shopping)
```

**Practice Exercise 9.4:**
Loop through a list:
```python
animals = ["cat", "dog", "bird"]
for animal in animals:
    print(animal)
```

**Mastery Check:** Can you create a list of 5 items and print each one using a loop? If yes, move to Step 10.

---

## STEP 10: Functions - Reusable Code Blocks

### What is a Function?
A function is a reusable block of code with a name. You define it once and can use it many times.

**Example 10.1: Simple function**
```python
def greet():
    print("Hello!")

greet()
greet()
greet()
```

**What happened?**
- `def` means "define a function"
- `greet` is the function name
- The indented code is what the function does
- Call the function by writing its name with `()`

**Example 10.2: Function with parameter**
```python
def greet(name):
    print("Hello, " + name)

greet("Alice")
greet("Bob")
```

**Example 10.3: Function that returns a value**
```python
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(sum_result)
```

**Practice Exercise 10.1:**
Type this 3 times:
```python
def say_hello():
    print("Hello, World!")

say_hello()
```

**Practice Exercise 10.2:**
Function with parameter:
```python
def introduce(name):
    print("My name is " + name)

introduce("Alice")
introduce("Bob")
```

**Practice Exercise 10.3:**
Function that calculates:
```python
def multiply(x, y):
    result = x * y
    return result

answer = multiply(4, 5)
print(answer)
```

**Practice Exercise 10.4:**
Create your own function:
```python
def greet_person(name, age):
    message = "Hello, " + name + ". You are " + str(age) + " years old."
    print(message)

greet_person("Charlie", 25)
```

**Mastery Check:** Can you write a function that takes two numbers and returns their sum? If yes, move to Step 11.

---

## STEP 11: Putting It All Together - Mini Projects

### Project 1: Simple Calculator
Combine everything you've learned!

```python
def calculator():
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        result = "Invalid operation"
    
    print("Result: " + str(result))

calculator()
```

**Practice:** Type this 3 times, then modify it to add more operations.

### Project 2: Number Guessing Game
```python
import random

secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("You win!")
else:
    print("Wrong! The number was " + str(secret_number))
```

**Practice:** Type this 3 times, then add a loop to let the user guess multiple times.

### Project 3: To-Do List
```python
todo_list = []

while True:
    task = input("Enter a task (or 'quit' to exit): ")
    if task == "quit":
        break
    todo_list.append(task)
    print("Your tasks:")
    for i, task in enumerate(todo_list):
        print(str(i + 1) + ". " + task)
```

**Practice:** Type this 3 times, then add features to remove tasks.

---

## STEP 12: Common Patterns to Master

### Pattern 1: Input Validation
```python
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age_num = int(age)
        print("You are " + str(age_num) + " years old")
        break
    else:
        print("Please enter a valid number")
```

**Practice:** Type this 3 times, then create your own validation.

### Pattern 2: Counting Items
```python
numbers = [1, 2, 3, 4, 5]
count = 0
for num in numbers:
    count = count + 1
print("Total items: " + str(count))
```

**Practice:** Type this 3 times, then count items matching a condition.

### Pattern 3: Finding Maximum
```python
numbers = [5, 2, 8, 1, 9]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print("Maximum: " + str(maximum))
```

**Practice:** Type this 3 times, then find the minimum.

---

## Final Mastery Checklist

Before moving to advanced topics, make sure you can do ALL of these without looking:

- [ ] Print messages and variables
- [ ] Create and use variables
- [ ] Combine strings
- [ ] Do math operations
- [ ] Get user input
- [ ] Convert between strings and numbers
- [ ] Write if/else statements
- [ ] Write for and while loops
- [ ] Create and use lists
- [ ] Define and call functions
- [ ] Combine all concepts in a program

---

## Next Steps After Mastery

Once you've typed every example 3-4 times and can write code without looking:

1. **Practice Daily:** Write 1 small program every day
2. **Build Projects:** Create your own programs combining concepts
3. **Read Code:** Look at other people's Python code
4. **Solve Problems:** Try coding challenges (start simple)
5. **Learn More:** Dictionaries, file handling, classes (but master basics first!)

---

## Remember:
- **Type, don't copy-paste** - Your fingers need to learn
- **Practice 3-4 times** - Repetition builds muscle memory
- **Understand why** - Don't just memorize, understand the logic
- **Build projects** - Apply what you learn immediately
- **Be patient** - Mastery takes time and practice

**You've got this! Keep practicing, and Python will become second nature.**


