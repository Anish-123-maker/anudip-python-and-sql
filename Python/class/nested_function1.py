def add(a,b,c):
    x=a+b+c
    print('The sum is {}'.format(x))
    def average(x):
        res=x/3
        return res
    print('The average of three numbers is {}'.format(average(x)))
    

"""def average(x):
    res=x/3
    return res"""


print('Enter three numbers')
a=int(input())
b=int(input())
c=int(input())
add(a,b,c)
