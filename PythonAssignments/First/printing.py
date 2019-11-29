data = "PYTHON"
x = " "
for i in range(1, len(data)+1):
    print(x*(len(data)-i), data[0:i])

for i in range(1, 5):
    print("*" * i)

for i in range(5, 0, -1):
    print("*" * i)

j = 0
for i in range(5, 0, -1):
    print(" " * j + "*" * i)
    j += 1

j = 4


