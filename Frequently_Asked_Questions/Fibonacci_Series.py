#  Fibonacci Series = A series of numbers in which each number is the sum of the two preceding numbers.

# 0 1 1 2 3 5 8 13 21 34 ... these are the fibonacci numbers.

# 0 = 0
# 1 = 1
# 2 => 0 + 1 = 2
# 3 => 1 + 2 = 3
# 5 => 2 + 3 = 5
# 8 => 3 + 5 = 8
# 13 => 5 + 8 = 13
# 21 => 8 + 13 = 21
# 34 => 13 + 21 = 34
# 55 => 21 + 34 = 55 ...

# -----------------------------------------------------

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(2,20):
    sum = n1+n2
    print(sum)
    n1 = n2
    n2 = sum



















