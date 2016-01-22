previousFib = 1
currentFib = 1
index = 2

thousand = 10**999
while (currentFib < thousand):
    temp = currentFib
    currentFib = previousFib + currentFib
    previousFib = temp
    index = index + 1

print index
