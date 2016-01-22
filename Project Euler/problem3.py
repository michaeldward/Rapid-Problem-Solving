import math

def largest_prime_factor(original):
    factors = []
    temp = math.floor(math.sqrt(original))
    while (temp > 1):
        if (original % temp == 0):
            factors.append(temp)
        temp = temp - 1

    for num in factors:
        for i in (2, num):
            if (num % i == 0):
                factors.remove(num)
                break
    return math.floor(max(factors))
    
print largest_prime_factor(600851475143)
