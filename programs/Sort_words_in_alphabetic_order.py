a = input("enter something here: ")

w = a.split()
print(w)
for i in range(len(w)):
    w[i] = w[i].lower()

#print(w)
w.sort()
#print(w)

for i in w:
    print(i)