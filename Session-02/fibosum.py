def fibosum(n):
    a = 0
    b = 1
    list = [a, b]
    for i in range(0, n-1):
        f = a + b
        list.append(f)
        a = b
        b = f
    return list

print("The sum of the first five series is ", sum(fibosum(5)))
print("The sum of the first ten series is ", sum(fibosum(10)))