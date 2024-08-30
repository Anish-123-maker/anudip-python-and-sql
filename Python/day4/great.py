num1 = 15
num2 = 25
num3 = 20
if num1 >= num2:
    if num1 >= num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 >= num3:
        greatest = num2
    else:
        greatest = num3
print(f"The greatest of {num1}, {num2}, and {num3} is {greatest}")
