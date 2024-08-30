"""The global keyword is used
to create global variables from a non-global scope, e.g. inside a function."""


a=100  #global variable
def abc():
    b=10   #local variable
    global a
    print("Local value b is ",b)
    print('Global value a is ',a)
    a+=10
    print('the value of a after operation is ',a)


#actual program starts here
print("the outside value of global before function call is ",a)
abc()
print('after function call the value of a is ',a)

