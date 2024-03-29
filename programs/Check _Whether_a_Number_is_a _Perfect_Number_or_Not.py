def is_perfect_number(num):
 sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
 return sum_of_divisors == num

number = 28
if is_perfect_number(number):
 print(number, "is a perfect number")
else:
 print(number, "is not a perfect number")