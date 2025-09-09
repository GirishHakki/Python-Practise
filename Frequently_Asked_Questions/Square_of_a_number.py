# program to find the square of a given number

# n = int(input("Enter the Number : "))
# print(n,"Square is", n**2)


#============================================================
# using math module

import math
n = int(input("Enter the Number : "))

res = math.pow(n, 2)
print(int(res))  # Convert to int if needed