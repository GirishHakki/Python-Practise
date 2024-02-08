for row in range(7):
    for col in range(5):
        if (col==0) or (row+col==4 and row<4) or (col==row-2 and row>3):
            print("*",end=" ")
        else:
            print(end="  ")
    print()