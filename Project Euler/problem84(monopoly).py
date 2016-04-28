import random

def move_forward(loc, move):
    loc = loc + move
    if loc > 39:
        loc = loc - 39
    if loc < 0:
        loc = loc + 39
    return loc

def community_chest(loc):
    card = random.randint(1, 16)
    if card == 1: #advance to GO
        return 0
    elif card == 2: #go to JAIL
        return 10
    else:
        return loc

def chance(loc):
    rr = [5, 15, 25, 35]
    uu = [12, 28]
    card = random.randint(1, 16)
    if card == 1: #advance to GO
        return 0
    elif card == 2: #go to JAIL
        return 10
    elif card == 3: #go to C1
        return 11
    elif card == 4: #go to E3
        return 24
    elif card == 5: #go to H2
        return 39
    elif card == 6: #go to R1
        return 5
    elif card == 7 or card == 8: #go to next R
        while loc not in rr:
            loc = move_forward(loc, 1)
    elif card == 9: #go to next U
        while loc not in uu:
            loc = move_forward(loc, 1)
    elif card == 10:
        loc = move_forward (loc, -3)
    return loc

def check_space(loc):
    if loc == 30: #G2J
        return 10
    elif loc == 2 or loc == 17 or loc == 33:
        return community_chest(loc)
    elif loc == 7 or loc == 22 or loc == 36:
        return chance(loc)
    else:
        return loc


spaces = []
loc = 0
dd = 0
for x in range(0, 40):
    spaces.append(0)

for y in range(0, 100000):
    
    #roll the dice and add together
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 == d2:
        ++dd
    else:
        dd = 0
    roll = d1 + d2
    #advance player
    loc = move_forward(loc, roll)
    if dd == 3:
        loc = 10
        dd = 0

    #check space to see if more moves required
    loc = check_space(loc)
    #increment current space to array
    spaces[loc] = spaces[loc] + 1

n1 = 0
nn1 = 0
n2 = 0
nn2 = 0
n3 = 0
nn3 = 0

for x in range(0, 39):
    if spaces[x] > nn1:
        nn1 = spaces[x]
        n1 = x
spaces[n1] = 0
for x in range(0, 39):
    if spaces[x] > nn2:
        nn2 = spaces[x]
        n2 = x
spaces[n2] = 0
for x in range(0, 39):
    if spaces[x] > nn3:
        nn3 = spaces[x]
        n3 = x
nn = ""
if len(str(n1)) == 1:
    nn = nn + "0"
nn = nn + str(n1)
if len(str(n2)) == 1:
    nn = nn + "0"
nn = nn + str(n2)
if len(str(n3)) == 1:
    nn = nn + "0"
nn = nn + str(n3)
print nn


    
