# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters using the replace method
cleaned_string = string.replace("\n", " ")

# Alternatively, you can strip leading/trailing whitespace
cleaned_string = cleaned_string.strip()

# Print the cleaned string
print(cleaned_string)

