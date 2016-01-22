def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
def reverse(n):
    x = str(n)[::-1]
    return int(x)

lychrel = 0
for x in range(10, 10000):
    lychrelFound = True
    z = x + reverse(x)
    for y in range(1, 50):
        if palindrome(z):
            lychrelFound = False
            break
        else:
            z = z + reverse(z)
    if lychrelFound:
        lychrel = lychrel + 1
print lychrel
