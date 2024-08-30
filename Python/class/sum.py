number = input("Enter a number: ")

sum_of_digits = 0

index = 0

while index < len(number):
    sum_of_digits += int(number[index])
    index += 1

print(f"The sum of the digits is: {sum_of_digits}")
