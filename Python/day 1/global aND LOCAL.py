x="I am Global"
def loc():
    x="I am local"
    return x
print("global:",x)
print("local:",loc())