for row in range(6):
    for col in range(5):
        if (col==3) or (row==5) and (col>0 and col<4) or (row==4 and col==0):
            print("*",end=" ")
        else:
            print(end="  ")
    print()