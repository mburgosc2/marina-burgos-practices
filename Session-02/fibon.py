def fibon(n):
    a = 0
    b = 1
    list = [a, b]
    for i in range(0, n-1):
        f = a + b
        list.append(f)
        a = b
        b = f
    return list[-1]

print("The 5th term is ", fibon(5))
print("The 10th term is ", fibon(10))
print("The 15th term is ", fibon(15))