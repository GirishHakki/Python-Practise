# Fibonacci Sequence = addition of previous number and present number
# eg = 0, 1, 1, 2, 3, 5, 8, 13, 21,.......

# a = 0          a = b
# b = 1          b = c
# c = a+b        c = a + c


# here a = 0, b = 1 for fixed
a = 0
b = 1
num = int(input("enter a number to obtain fibonacci sequence: "))

if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a+b
        a = b
        b = c
        print(c)

