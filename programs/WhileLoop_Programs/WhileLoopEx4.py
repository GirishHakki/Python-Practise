# WAP which will generate all the even numbers within n in backward direction where n can be +ve

n = int(input("Enter a positive number: "))

if n > 0:
    print(f"Even numbers from {n} to 1 in reverse order:")
    print("-"*30)

    # If n is odd, start from the previous even number
    if n % 2 != 0:
        n = n - 1

    while n >= 2:
        print("{}".format(n))
        n = n - 2
else:
    print("enter a positive number")
