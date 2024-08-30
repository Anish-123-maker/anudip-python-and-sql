import re

# Function to check the validity of the password
def is_valid_password(password):
    # Check the length of the password (should be between 6 and 16 characters)
    if len(password) < 6 or len(password) > 16:
        return False
    # Check if the password contains at least one lowercase letter
    if not re.search("[a-z]", password):
        return False
    # Check if the password contains at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    # Check if the password contains at least one digit
    if not re.search("[0-9]", password):
        return False
    # Check if the password contains at least one special character
    if not re.search("[@#$%^&+=]", password):
        return False
    # If all checks pass, the password is valid
    return True

# Accept a password from the user
password = input("Enter a password: ")

# Validate the password
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be 6-16 characters long, include at least one lowercase letter, one uppercase letter, one digit, and one special character (@, #, $, %, ^, &, +, =).")

