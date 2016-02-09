def convertToBaseTen(size, base, numbers):
    result = 0
    for x in range(0, size):
        power = size - x - 1
        multiply = base ** power
        result += multiply * numbers[x]
    return result

def compare(xSize, xBase, xNums, ySize, yBase, yNums):
    xResult = convertToBaseTen(xSize, xBase, xNums)
    yResult = convertToBaseTen(ySize, yBase, yNums)
    if xResult > yResult:
        return '>'
    elif xResult < yResult:
        return '<'
    elif xResult == yResult:
        return '='


line0 = map(int, raw_input().split())
line1 = map(int, raw_input().split())
line2 = map(int, raw_input().split())
line3 = map(int, raw_input().split())

print compare(line0[0], line0[1], line1, line2[0], line2[1], line3)

#print convertToBaseTen(6, 7, [1, 1, 2, 1, 2, 1])
#print convertToBaseTen(6, 6, [2, 3, 2, 2, 2, 2])
#print compare(6, 7, [1, 1, 2, 1, 2, 1], 6, 6, [2, 3, 2, 2, 2, 2])

