def sum_of_cubes(n):
 return sum(i**3 for i in range(1, n+1))

n = 3
print("Sum of cubes of first", n, "natural numbers is:", sum_of_cubes(n))