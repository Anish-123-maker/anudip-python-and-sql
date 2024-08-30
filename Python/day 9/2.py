def remove_duplicates(input_string):
    words = input_string.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    result = ' '.join(unique_words)
    print(f"Output: {result}")

input_string = "String and String Function"
remove_duplicates(input_string)
