rows = int(input("Enter the number of rows: "))

# Outer for loop to handle number of rows
for i in range(rows, 0, -1):
    # Inner for loop to handle number of columns
    # values change according to the outer loop
    for j in range(0, i + 1):
        print(j, end=" ")

        # End line after each row
    print()