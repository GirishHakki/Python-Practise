def intersection(lst1, lst2):
 return list(set(lst1) & set(lst2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection of lists:", intersection(list1, list2))