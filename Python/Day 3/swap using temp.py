num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print('Old value of num1 is {} and num2 is {}'.format(num1, num2))
temp=num1
num1=num2
num2=temp
print('Old value of num1 is {} and num2 is {}'.format(num1, num2))