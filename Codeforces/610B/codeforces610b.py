def paint(jarNum, jars):
    squaresPainted = 0
    while (True):      
        for x in range (0, jarNum):
            if (jars[x] == 0):
                return squaresPainted
            else:
                squaresPainted = squaresPainted + 1
                jars[x] = jars[x] - 1
    return squaresPainted

n = raw_input()
n = int(n)
jars = map(int, raw_input().split())
print paint(n, jars)



