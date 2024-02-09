for row in range(6):
    for col in range(5):
        if (row-col==0 and row<3) or(row+col==4 and row<3) or (col==2 and row>1):
            print("*", end=" ")
        else:
            print(end="  ")
    print()
