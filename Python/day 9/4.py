def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in input_string if char in vowels)
    
    print(f"Total vowels are: {count}")

input_string = "Welcome to Python Assignment"
count_vowels(input_string)
