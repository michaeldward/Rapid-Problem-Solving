def number_of_rectangles(n):
    total = 0
    if n % 2 is 0 and n > 3:
        total = (n - 1) / 4
    return total

n = raw_input()
print number_of_rectangles(int(n))
