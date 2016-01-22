def find_prime_factors(number):
    result = []
    i = 2
    while (i < number):
        if (number % i == 0):
            result.append(i)
            number /= i
        else:
            i += 1
    result.append(number)
    return result



def smallest_number_divisible(number):
    factors = []
    for i in range(2, number + 1):
        result = find_prime_factors(i)
        for j in range(2, number + 1):
            x = result.count(j) - factors.count(j)
            while (x > 0):
                factors.append(j)
                x -= 1
    smallestNumber = 1
    for num in factors:
        smallestNumber *= num
    return smallestNumber

print smallest_number_divisible(20)
    
