def difference(x):
    first = 0
    for i in range(1, x + 1):
        first += i ** 2
    second = 0
    for i in range(1, x + 1):
        second += i
    second = second ** 2
    return second - first
print difference(100)
