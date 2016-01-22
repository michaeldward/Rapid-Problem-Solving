numbers = map(int, raw_input().split())
rows = numbers[0]
cols = numbers[1]
good = True
previousRow = -1

for x in range (1, rows + 1):
    n = raw_input()
    nums = [int(d) for d in str(n)]
    previousNum = -1
    if len(nums) is not cols:
        good = False
        break
    if previousRow is -1:
        previousRow = nums[0]
    elif previousRow is nums[0]:
        good = False
        break
    else:
        previousRow = nums[0]
    for y in nums:
        if previousNum is -1:
            previousNum = y
        elif previousNum is not y:
            good = False
            break
        else:
            previousNum = y
    

if good:
    print "YES"
else:
    print "NO"
