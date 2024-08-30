def count_chars_digits_symbols(input_string):
    letters = digits = symbols = 0
    for char in input_string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():
            symbols += 1
    
    print(f"Chars = {letters} Digits = {digits} Symbol = {symbols}")

input_string = "P@#yn26at^&i5ve"
count_chars_digits_symbols(input_string)
