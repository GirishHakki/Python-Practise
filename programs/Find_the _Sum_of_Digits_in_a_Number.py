def sum_of_digits(num):

 return sum(int(digit) for digit in str(num))

number = int(input("Enter the number: "))
print("Sum of digits in", number, "is:", sum_of_digits(number))