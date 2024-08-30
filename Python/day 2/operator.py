
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '//':
        return num1 // num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return "Invalid operator"


try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    op = input("Enter the operator (+, -, *, //, /, %): ")

    # Performing the calculation and displaying the result
    result = calculate(number1, number2, op)
    print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
