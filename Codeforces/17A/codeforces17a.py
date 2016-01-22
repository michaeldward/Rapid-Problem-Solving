def is_prime(x):
    end = x / 2 + 1
    for y in range(2, end):
        if x % y is 0:
            return False
    return True

def primes_until_num(x):
    primes = []
    for y in range(2, x + 1):
        if is_prime(y):
            primes.append(y)
    return primes

numbers = map(int, raw_input().split())
n = numbers[0]
k = numbers[1]
good = True

if n > 1000 or n < 2:
    good = False
if k > 1000 or k < 0:
    good = False

numOfPrimes = 0
kFound = 0
primes = []
for x in range (2, n + 1):
    if is_prime(x):
        numOfPrimes = numOfPrimes + 1
        primes.append(x)
if numOfPrimes < k:
    good = False
for x in primes:
    primesUntilNum = primes_until_num(x)
    #print x
    for y in range (0, len(primesUntilNum) - 1):
        #print y
        if x is (primesUntilNum[y] + primesUntilNum[y + 1] + 1):
            kFound = kFound + 1
            #print x, primesUntilNum[y], primesUntilNum[y + 1], 1, kFound
            break
if kFound < k:
    good = False
    #print kFound, k
    #print primes_until_num(296)

    
if good:
    print "YES"
else:
    print "NO"
