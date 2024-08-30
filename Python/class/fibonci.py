def print_fibonacci_series(n):
    a, b = 0, 1
    print(a, b, end=" ")
    
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
n = int(input("Enter the number of terms in the Fibonacci series: "))
print_fibonacci_series(n)
