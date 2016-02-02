numbers = map(int, raw_input().split())
needed = map(int, raw_input().split())
blue = numbers[0]
violet = numbers[1]
orange = numbers[2]
neededBlue = needed[0]
neededViolet = needed[1]
neededOrange = needed[2]

excessBlue = blue - neededBlue
excessViolet = violet - neededViolet
excessOrange = orange - neededOrange


def spheres(excessBlue, excessViolet, excessOrange):
    extraSpheres = 0
    while (excessBlue > 1):
        excessBlue = excessBlue - 2
        extraSpheres = extraSpheres + 1
    while (excessViolet > 1):
        excessViolet = excessViolet - 2
        extraSpheres = extraSpheres + 1
    while (excessOrange > 1):
        excessOrange = excessOrange - 2
        extraSpheres = extraSpheres + 1
    while (excessOrange < 0):
        if (extraSpheres > 0):
            excessOrange = excessOrange + 1
            extraSpheres = extraSpheres - 1
        else:
            return 'No'
    while (excessViolet < 0):
        if (extraSpheres > 0):
            excessViolet = excessViolet + 1
            extraSpheres = extraSpheres - 1
        else:
            return 'No'
    while (excessBlue < 0):
        if (extraSpheres > 0):
            excessBlue = excessBlue + 1
            extraSpheres = extraSpheres - 1
        else:
            return 'No'
    return 'Yes'
print spheres(excessBlue, excessViolet, excessOrange)
