#Taking input from user
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1       #
n = num
while n > 0:                
    factorial *= n
    n -= 1
print(f"The factorial of {num} is {factorial}")     #Print the answer