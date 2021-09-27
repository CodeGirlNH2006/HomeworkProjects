# Ask user for two numbers
num1 = input("First number?")
num2 = input("Second number?")
# Calculate sum
sum = int(num1) + int(num2)
# Calculate product
prod = int(num1) * int(num2)
# Create a loop that does the following until the product and sum are the same
while sum != prod:
    # Display sum and product
    print("Sum and product are not equal, as sum = " + str(sum) + " and product = " + str(prod) + ". Try again.")
    # Ask for two more numbers
    num1 = input("First number?")
    num2 = input("Second number?")
    # Recalculate sum and product
    sum = int(num1) + int(num2)
    prod = int(num1) * int(num2)
# If their sum and their product are equal - tell the user
print("Sum and product both equal " + str(sum) + "!")