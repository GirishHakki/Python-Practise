# solution 1 (using third variable)

# x = 10
# y = 20

# here temp is 3rd variable
# temp = x
# print("the value of temp variable is", temp)
#
# x = y
# print("the value of x is", x)
#
# y = temp
# print("the value of y is", y)

# solution 2 ( without using third variable)
x = 10
y = 20

x, y = y, x

print("The value of x is", x)
print("The value of y is", y)