for row in range(6):
    for col in range(6):
        if (row-col==0) or (row+col==5):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
