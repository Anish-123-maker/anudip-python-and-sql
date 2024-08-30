# Function to calculate factorial using a while loop
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")
