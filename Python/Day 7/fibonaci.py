# Function to generate Fibonacci series up to a maximum value
def fibonacci_series(max_value):
    a, b = 0, 1
    while a <= max_value:
        print(a, end=" ")
        a, b = b, a + b

# Generate and print the Fibonacci series up to 50
fibonacci_series(50)
