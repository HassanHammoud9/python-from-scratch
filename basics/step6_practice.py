# STEP 6 PRACTICE: Converting Input to Numbers
# Type each exercise 3-4 times, run them with different numbers

# # Exercise 6.1: Doubling a number
# num = input("Enter a number: ")
# doubled = int(num) * 2
# print("Double is " + str(doubled))

# Exercise 6.2: Sum of two numbers
# a = input("First number: ")
# b = input("Second number: ")
# sum_result = int(a) + int(b)
# print("Sum: " + str(sum_result))

# # Exercise 6.3: Area of circle
# radius = input("Enter radius: ")
# area = float(radius) * float(radius) * 3.14
# print("Area is " + str(area))

# # Exercise 6.4: Bill with tip
# bill = input("Enter bill amount: ")
# tip_percent = input("Enter tip percent: ")
# bill_num = float(bill)
# tip_num = float(tip_percent)
# tip_amount = bill_num * (tip_num / 100)
# total = bill_num + tip_amount
# print("Total: " + str(total))

# -------------------------------------------------------------


# when you want to do a calculation you basically have to convert it to an integer and when printing it you have to convert it to a string.
num = input("Enter a number: ")
print(f"this is the doubled number {str(int(num)*2)}")