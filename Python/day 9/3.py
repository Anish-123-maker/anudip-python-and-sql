def count_char_types(input_string):
    uppercase = lowercase = numbers = special_chars = 0
    
    for char in input_string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        elif not char.isspace():
            special_chars += 1
    
    print(f"UpperCase : {uppercase} LowerCase : {lowercase} NumberCase : {numbers} SpecialCase : {special_chars}")

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
count_char_types(input_string)
