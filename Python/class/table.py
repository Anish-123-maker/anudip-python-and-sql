# Function to print multiplication table
def print_multiplication_table(number, up_to=10):
    print(f"Multiplication Table for {number}:\n")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Input: Ask the user for the number
number = int(input("Enter the number to print its multiplication table: "))

# Print the multiplication table
print_multiplication_table(number)
