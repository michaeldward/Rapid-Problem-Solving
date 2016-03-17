def find_clappers(people):
    standing = 0
    needed = 0
    for x in range(0, len(people)):
        if not people[x].isdigit():
            continue
        val = int(people[x])
        if val is 0:
            if standing < x + 1:
                needed = needed + 1
                standing = standing + 1
        else:
            if standing < x:
                needed = needed + 1
                standing = standing + val
            else:
                standing = standing + val
    return needed
answers = []
#f = open('A-large-practice.in')
#r = open('A-large-practice.out', 'a')
total = int(raw_input())
#total = int(f.readline())
for x in range(0, total):
    dudes = raw_input().split(' ')
    #dudes = f.readline().split(' ')
    answers.append(find_clappers(dudes[1]))

for x in range(0, len(answers)):
    #r.write("Case #" + str(x + 1) + ": " + str(answers[x]) + '\n')
    print("Case #" + str(x + 1) + ": " + str(answers[x]))
