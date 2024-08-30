int1=int(input("Enter first number"))
int2=int(input("Enter second number"))
print('Old value of int1 is {} and int2 is {}'.format(int1, int2))

int1 = int1 + int2  # add both numbers, store result in int1
int2 = int1 - int2  # subtract int2 from int1, store result in int2
int1 = int1 - int2  # subtract int2 from int1 again, swap values

print('New value of int1 is {} and int2 is {}'.format(int1, int2))