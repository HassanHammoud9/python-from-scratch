# STEP 12 PRACTICE: Common Patterns
# Type each pattern 3-4 times, then create variations

# Pattern 1: Input Validation
def validate_age():
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age_num = int(age)
            print("You are " + str(age_num) + " years old")
            break
        else:
            print("Please enter a valid number")

# Uncomment to run:
# validate_age()

# Pattern 2: Counting Items
def count_items():
    numbers = [1, 2, 3, 4, 5]
    count = 0
    for num in numbers:
        count = count + 1
    print("Total items: " + str(count))

# Uncomment to run:
# count_items()

# Pattern 3: Finding Maximum
def find_maximum():
    numbers = [5, 2, 89, 1, 9]
    maximum = numbers[0]
    for num in numbers:
        if num> maximum:
            maximum = num
    print("Maximum: " + str(maximum))

# Uncomment to run:
# find_maximum()


