for row in range(7):
    for col in range(5):
        if (row==6 or col==2) or (col==1 and row==1):
            print("*", end=" ")
        else:
            print(end="  ")
    print()