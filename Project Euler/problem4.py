palindrome = 0

for num1 in range(100, 999):
    for num2 in range(100, 999):
        num3 = num1 * num2
        if str(num3) == str(num3)[::-1]:
            if num3 > palindrome:
                palindrome = num3

print palindrome
