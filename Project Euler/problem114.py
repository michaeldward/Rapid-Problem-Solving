def unit(width):
    total = 0
    if width is 3:
        return 2
    elif width < 3:
        return 1
    elif width < 1:
        return 0
    else:
        for redSize in range(3, width):
            total = width + 1 - redSize
            for redNum in range(1, width/redSize):
                #calculate the stuff
        total = total + 2
print unit(50)
