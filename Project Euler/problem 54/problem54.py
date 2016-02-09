# 1 high value cards
# 2 one pair
# 3 two pairs
# 4 three of a kind
# 5 straight
# 6 flush
# 7 full house
# 8 four of a kind
# 9 straight flush
# 10 royal flush
# 1-14 card

def value_card(card):
    if card is 'A':
        return 14
    elif card is 'K':
        return 13
    elif card is 'Q':
        return 12
    elif card is 'J':
        return 11
    elif card is 'T':
        return 10
    else:
        return int(card)

def high_card(cards):
    highest = 0
    for x in cards:
        value = value_card(x[0])
        if  value > highest:
            highest = value
    return highest

def one_pair(cards):
    pairs = []
    y = []
    for x in cards:
        if x[0] not in y:
            y.append(x[0])
        else:
            pairs.append(x[0])
    return high_card(pairs)

def two_pairs(cards):
    pairs = []
    y = []
    for x in cards:
        if x[0] not in y:
            y.append(x[0])
        elif x[0] not in pairs:
            pairs.append(x[0])
    if len(pairs) > 1:
        return high_card(pairs)
    else:
        return 0
def three_kind(cards):
    pairs = []
    three = []
    y = []
    for x in cards:
        if x[0] in pairs:
            three.append(x[0])
        elif x[0] in y:
            pairs.append(x[0])
        else:
            y.append(x[0])
    return high_card(three)
def four_kind(cards):
    four = []
    three = []
    pairs = []
    y = []
    for x in cards:
        if x[0] in three:
            four.append(x[0])
        elif x[0] in pairs:
            three.append(x[0])
        elif x[0] in y:
            pairs.append(x[0])
        else:
            y.append(x[0])
    return high_card(four)
def straight(cards):
    values = []
    for x in cards:
        values.append(value_card(x[0]))
    values.sort()
    for x in range(1, len(values)):
        if (values[x] - values[x - 1]) is not 1:
            return 0
    return high_card(cards)
def flush(cards):
    suit = cards[0][1]
    for x in cards:
        if x[1] is not suit:
            return 0
    return high_card(cards)
def full_house(cards):
    x = three_kind(cards)
    y = one_pair(cards)
    if x is 0:
        return 0
    elif  y is 0:
        return 0
    elif x > y:
        return x
    else:
        return y
def straight_flush(cards):
    x = straight(cards)
    y = flush(cards)
    if x is 0:
        return 0
    elif y is 0:
        return 0
    elif x > y:
        return x
    else:
        return y
def royal_flush(cards):
    x = flush(cards)
    if x is 0:
        return 0
    else:
        royal = ['T', 'J', 'Q', 'K', 'A']
        for y in cards:
            if y[0] in royal:
                royal.remove(y[0])
            else:
                return 0
    return x
def determine_winner(cards):
    cards = cards.split(' ')
    player1 = cards[:len(cards)/2]
    player2 = cards[len(cards)/2:]
    if royal_flush(player1) or royal_flush(player2):
        if royal_flush(player1) > royal_flush(player2):
            return 1
        elif royal_flush(player2) > royal_flush(player1):
            return 2
        return determine_high(player1, player2)
    if straight_flush(player1) or straight_flush(player2):
        if straight_flush(player1) > straight_flush(player2):
            return 1
        elif straight_flush(player2) > straight_flush(player1):
            return 2
        return determine_high(player1, player2)
    if four_kind(player1) or four_kind(player2):
        if four_kind(player1) > four_kind(player2):
            return 1
        elif four_kind(player2) > four_kind(player1):
            return 2
        return determine_high(player1, player2)
    if full_house(player1) or full_house(player2):
        if full_house(player1) > full_house(player2):
            return 1
        elif full_house(player2) > full_house(player1):
            return 2
        return determine_high(player1, player2)
    if flush(player1) or flush(player2):
        if flush(player1) > flush(player2):
            return 1
        elif flush(player2) > flush(player1):
            return 2
        return determine_high(player1, player2)
    if straight(player1) or straight(player2):
        if straight(player1) > straight(player2):
            return 1
        elif straight(player2) > straight(player1):
            return 2
        return determine_high(player1, player2)
    if three_kind(player1) or three_kind(player2):
        if three_kind(player1) > three_kind(player2):
            return 1
        elif three_kind(player2) > three_kind(player1):
            return 2
        return determine_high(player1, player2)
    if two_pairs(player1) or two_pairs(player2):
        if two_pairs(player1) > two_pairs(player2):
            return 1
        elif two_pairs(player2) > two_pairs(player1):
            return 2
        return determine_high(player1, player2)
    if one_pair(player1) or one_pair(player2):
        if one_pair(player1) > one_pair(player2):
            return 1
        elif one_pair(player2) > one_pair(player1):
            return 2
        return determine_high(player1, player2)
    return determine_high(player1, player2)

def determine_high(player1, player2):
    if high_card(player1) > high_card(player2):
        return 1
    elif high_card(player2) > high_card(player1):
        return 2
    else:
        player1.remove(high_card(player1))
        player2.remove(high_card(player2))
        return determine_high(player1, player2)

f = open('input.txt', 'r')
       
content = f.readlines()
oneWins = 0
twoWins = 0
for x in content:
    if determine_winner(x) is 1:
        oneWins = oneWins + 1
    else:
        twoWins = twoWins + 1
print oneWins
