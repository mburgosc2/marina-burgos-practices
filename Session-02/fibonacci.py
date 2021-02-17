a = 0
b = 1
list = [a, b]
limit = 11
for i in range(0, limit - 2):
    f = a + b
    list.append(f)
    a = b
    b = f

for i in list:
    print(i, end=" ")