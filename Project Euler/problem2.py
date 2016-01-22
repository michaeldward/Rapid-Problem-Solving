total = 0
currentNum = 1
previousNum = 1
while (currentNum < 4000000):
    temp = currentNum
    currentNum = currentNum + previousNum
    previousNum = temp
    if (currentNum % 2 == 0):
        total += currentNum
print total
