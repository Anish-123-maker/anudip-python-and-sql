ch = 65  # ASCII value of 'A'

for i in range(1, 6):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
