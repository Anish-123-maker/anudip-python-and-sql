n = 5  # The number of rows in the pattern

for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")
    
    # Move to the next line after each row
    print()

