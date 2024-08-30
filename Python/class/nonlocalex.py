"""The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.

Use the keyword nonlocal to declare that the variable is not local."""

def xyz():    #outer function
  x = "John"   #local variable
  def abc():      #inner function
    nonlocal x
    x = "hello"
  abc() 
  return x

print(xyz())
