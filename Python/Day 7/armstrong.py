# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to iterate through digits
    digits = str(number)
    # Calculate the number of digits
    num_digits = len(digits)
    # Calculate the sum of the powers of each digit
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    # Check if the sum of powers equals the original number
    return sum_of_powers == number

# Accept input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
