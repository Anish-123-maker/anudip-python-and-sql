# Function to check if a number is an Armstrong number
def is_armstrong(number):
    original_number = number
    num_digits = len(str(number))
    sum_of_powers = 0
    
    while number > 0:
        digit = number % 10
        sum_of_powers += digit ** num_digits
        number = number // 10
    
    return original_number == sum_of_powers

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
