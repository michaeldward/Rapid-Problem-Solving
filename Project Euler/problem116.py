def triominoes(m, n):
    if m * n % 3 != 0: return 1
    if m is 3 and n is 3: return 14
    elif n in (1,3) and m in (1,3) and n != m: return 1
    elif n in (2,3) and m in (2,3) and n != m: return 3
    if (m is 6 and n is 2) or (n is 6 and m is 2): return 11
    total = 1
    for i in range(1, n):
        total = total * triominoes(m, n-i)
    for i in range(1, m):
        total = total * triominoes(m-i, n)
    for i in range(1, n):
        for j in range(1, m):
            total = total + triominoes(m-i, n-i)
    return total

print triominoes(9, 3)
