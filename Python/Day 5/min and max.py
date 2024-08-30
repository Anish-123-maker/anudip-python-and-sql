import random
min_value = 1
max_value = 100
a = [random.randint(min_value, max_value) for _ in range(5)]
print(a)
print(f"minimum number of {a} is {min(a)}")
print(f"maximum number of {a} is {max(a)}")