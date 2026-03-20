# # STEP 10 PRACTICE: Functions
# # Type each exercise 3-4 times

# # Exercise 10.1: Simple function
# def say_hello():
#     print("Hello, World!")

# say_hello()

# # Exercise 10.2: Function with parameter
# def introduce(name):
#     print("My name is " + name)

# introduce("Alice")
# introduce("Bob")

# Exercise 10.3: Function that calculates
def multiply(x, y):
    result = x * y
    return result

answer = multiply(4, 5)
print(answer)

# # Exercise 10.4: Function with multiple parameters
def greet_person(name, age):
    message = "Hello, " + name + ". You are " + str(age) + " years old."
    print(message)

greet_person("Charlie", 25)