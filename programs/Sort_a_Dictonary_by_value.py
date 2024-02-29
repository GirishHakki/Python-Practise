marks = {"Girish": 23, "Lisa": 21, "Sid": 48}
print(marks)

#solution 1 (sort the dictonary based on value)
sv = sorted(marks.items(), key= lambda X : X[1])
print(sv)

# #solution 2 (sort only the values)
# v = sorted(marks.values())
# print(v)