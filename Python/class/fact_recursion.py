#program to find the factorial of a number.
#5!-> 5*4*3*2*1

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)



x=int(input('Enter the number'))
res=fact(x)
print('The factorial of {} is {}'.format(x,res))
