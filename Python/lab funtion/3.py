def multiply(a, b=1):
    return a * b
a=input("enter the number: ")
b=input("if you want to multiply another number then enter the number else leave blank")
if b==" ":
    # Using both arguments
    result1 = multiply(a, b)
    print(result1)  
else:
    # Using only one argument, the second defaults to 1
    result2 = multiply(a)
    print(result2)  


