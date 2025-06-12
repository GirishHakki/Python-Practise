# Program for generating n to 1 where n is +VE

n = int(input("Enter How many numbers u want to generate : "))
if (n<=0):
    print('{} is invalid input'.format(n))
else:
    print("-"*20)
    print("Numbers from {} to {}".format(n,1))
    print("-" * 20)
    i=n #initialization part
    while(i>=1):
        print("\t{}".format(i))
        i=i-1
    else:
        print("-"*20)

