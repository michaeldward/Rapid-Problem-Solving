number = int(raw_input())
cars = map(int, raw_input().split())
transforms = 0
index = 0
numberneeded = 1
passed = []

while(index < number):
    if cars[index] is numberneeded:
        numberneeded = numberneeded + 1
        index = index + 1
    elif numberneeded in passed:
        numberneeded = numberneeded + 1
    else:
        transforms = transforms + 1
        passed.append(cars[index])
        index = index + 1
print transforms
