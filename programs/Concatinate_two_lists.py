# Solution 1 using + operation
# l1 = [3,6,8,2,"a","j"]
# l2 = [3,6,"h","f","a","j"]
#
# l12 = l1+l2
# print(l12)

# solution 2 with unique values
l1 = [3,6,8,2,"a","j"]
l2 = [3,6,"h","f","a","j"]

l12 = list(set(l1+l2))
print(l12)