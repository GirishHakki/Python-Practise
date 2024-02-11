# solution 1 using for loop
num = int(input("Entert a number here: "))

fact = 1
if num<0:
    print("factorial of 0 does not exists")
if num == 0:
    print("factorial of 0 is", 1)
if num>0:
    for i in range(1, num+1):
        fact = fact*i
print("The factorial of th given number is", fact)








# solution 2 using Recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))  #eg= a=3 -> ((3)*fact(3-1) = 3*2 = 6
num = int(input("Entert a number here: "))

result = fact(num)
print("The factorial of th given number is", result)
