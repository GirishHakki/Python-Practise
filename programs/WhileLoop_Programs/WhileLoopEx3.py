# WAP which will generate all the even numbers within n in forward direction where n can be +ve

# Input from user
n = int(input("Enter a positive number: "))
if n > 0:
    print(f"Even numbers from 1 to {n} are:")
    i =2
    while(i<=n):
        # print(i, end=" ")
        print("{}".format(i))
        i = i+2
else:
    print("enter a positive number")


