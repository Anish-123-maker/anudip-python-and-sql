def alternate_characters(text):
    result = []
    i, j = 0, len(text) - 1

    while i <= j:
        if i % 2 == 0:
            result.append(text[i])
        else:
            result.append(text[j])

        if i != j: 
            if i % 2 == 0:
                result.append(text[j])
            else:
                result.append(text[i])

        i += 1
        j -= 1

    return ''.join(result)


text = "DataScience"
output = alternate_characters(text)
print(output)
