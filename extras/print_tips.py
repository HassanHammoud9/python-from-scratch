# PRINT STATEMENT TIPS
# Your print statement works, but here are some cleaner ways to write it

# Your current code (works fine!):
num1 = 15
num2 = 7
sum_result = num1 + num2  # Changed 'sum' to 'sum_result' (better practice)
diff = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Option 1: Your way (works perfectly!)
print("The sum is "+str(sum_result)+","+" and the difference is: "+ str(diff)+","+" and the product is: "+ str(product) + ","+ "and finally the quotient is: " + str(quotient))

# Option 2: Using commas (easier to read)
print("The sum is", sum_result, ", and the difference is:", diff, ", and the product is:", product, ", and finally the quotient is:", quotient)

# Option 3: Using f-strings (modern Python way - you'll learn this later)
# print(f"The sum is {sum_result}, and the difference is: {diff}, and the product is: {product}, and finally the quotient is: {quotient}")

# Option 4: Multiple print statements (clearest)
print("The sum is", sum_result)
print("The difference is:", diff)
print("The product is:", product)
print("The quotient is:", quotient)

# All of these work! Use whichever feels most comfortable.
# Your way is perfectly fine - just remember to use str() when combining with +
