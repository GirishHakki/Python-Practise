def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

number = 12345
print("Number of digits in", number, "is:", count_digits(number))