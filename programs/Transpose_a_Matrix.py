# Transpose Matrix = converting row matrix into column matrix or vice versa

# solution 1 using for loop

# A = [[1,2,3],
#      [4,5,6]]
# T = [[0,0],
#      [0,0],
#      [0,0]]
#
# for i in range (len(A)):
#     for j in range (len(A[0])):
#         print(j)
#         T[j][i] = A[i][j]
#
# for i in T:
#     print(i)

# solution 2 using for list comprehension

A = [[1,2,3],
     [4,5,6]]
T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

for i in T:
    print(i)