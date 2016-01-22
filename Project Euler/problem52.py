def permutation(first, second):
    firstLetters = []
    secondLetters = []
    for x in str(first):
        firstLetters.append(x)
    for y in str(second):
        secondLetters.append(y)
    for x in firstLetters:
        if firstLetters.count(x) is not secondLetters.count(x):
            return False
    return True

def check_number(n):
    done = True
    if not permutation(n, 2*n):
        done = False
    if not permutation(n, 3*n):
        done = False
    if not permutation(n, 4*n):
        done = False
    if not permutation(n, 5*n):
        done = False
    if not permutation(n, 6*n):
        done = False
    return done
            

x = 125874
done = False
while not done:
    if not check_number(x):
        x = x + 1
    else:
        done = True
        print x
