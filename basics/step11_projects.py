# STEP 11 PRACTICE: Mini Projects
# Project 1: Number Guessing Game
import random

def guessing_game():
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == secret_number:
        print("You win!")
    else:
        print("Wrong! The number was " + str(secret_number))

# Uncomment to run:
# guessing_game()

# Project 2: To-Do List
def todo_list():
    tasks = []
    
    while True:
        task = input("Enter a task (or 'quit' to exit): ")
        if task == "quit":
            break
        tasks.append(task)
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(str(i + 1) + ". " + task)

# Uncomment to run:
# todo_list()
# Type each project 3-4 times, then modify and improve them

# Project 3: Simple Calculator
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

# Uncomment to run:
# calculator()

