n=int(input("enter the number till you find even numbers: "))
for n in range(0, n+1, 1):
    if n%2==0:
        print(n)
    