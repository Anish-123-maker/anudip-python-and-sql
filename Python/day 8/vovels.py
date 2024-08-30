def count_vowels(text):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = "Welcome to python Training"
vowel_count = count_vowels(text)
print(f"The number of vowels in '{text}' is {vowel_count}")