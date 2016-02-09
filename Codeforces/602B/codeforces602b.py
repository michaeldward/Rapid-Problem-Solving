number = int(raw_input())
line = map(int, raw_input().split())

def find_largest_range(size, numbers):
    longestRange = 0 #longest range so far
    beginRange1 = 0 #begin of current number - 1
    beginRange2 = 0 #begin of current number - 2
    for x in range(1, size):
        
        if numbers[x] > numbers[x - 1] + 1: #next number is at least 2 bigger
            if x - beginRange2 > longestRange:
                longestRange = x - beginRange2
                #print "longest range now " + str(longestRange) + " at position " + str(x)
            beginRange2 = numbers[x - 1]
            beginRange1 = beginRange2
        elif numbers[x] > numbers[x - 1]: #next number is bigger
            if x - beginRange2 + 1 > longestRange:
                longestRange = x - beginRange2 + 1
                #print "longest range now " + str(longestRange) + " at position " + str(x)
            beginRange2 = beginRange1
            beginRange1 = numbers[x - 1]
        
        if numbers[x] < numbers[x - 1] -1: #next number is at least 2 smaller
            if x - beginRange2 > longestRange:
                longestRange = x - beginRange2
                #print "longest range now " + str(longestRange) + " at position " + str(x)
            beginRange2 = numbers[x - 1]
            beginRange1 = beginRange2
        elif numbers[x] < numbers[x - 1]: #next number is smaller
            if x - beginRange2 + 1 > longestRange:
                longestRange = x - beginRange2 + 1
                #print "longest range now " + str(longestRange) + " at position " + str(x)
            beginRange2 = beginRange1
            beginRange1 = numbers[x - 1]
    return longestRange

print find_largest_range(number, line)
