# Function to check if a number is a palindrome
def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    
    return original_number == reversed_number

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
