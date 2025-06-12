# Program for generating 1 to n numbers when n is +ve


n = int(input("Enter How Many Numbers u want to generate: "))
if (n<=0):
    print("{} is invalid input".format(n))
else:
    #login for generating 1 to n numbers
    i=1 #initialization part
    while (i<=n):
        print("{}".format(i))
        i = i+1 #updation part
print("Program execution completed")



