def traverse_reverse_with_index(input_list):
    # Traverse the list in reverse order
    for index, item in enumerate(reversed(input_list)):
        # Calculate the original index in the reversed list
        original_index = len(input_list) - 1 - index
        print(f"Original index {original_index}: {item}")

# Example list
input_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
traverse_reverse_with_index(input_list)
