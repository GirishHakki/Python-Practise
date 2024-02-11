# program to check ArmStrong Number

# Armstrong number => LHS = RHS
# eg => 153 = (1*1*1) + (5*5*5) + (3*3*3)
#       153 =  1 + 125 + 27
#       153 =  153 #LHS = RHS

# eg 2=> 52 = (5*5) + (2*2)
#        52 = 25 + 9
#        52 = 34  #here LHS != RHS


# this is only for 3 digit
# num = int(input("enter a number here: "))
# sum = 0
# temp = num
#
# while temp > 0:
#     digit = temp%10
#     cube = digit ** 3
#     sum = sum + cube
#     temp //=10
#
# if sum == num:
#     print('It is an Armstrong Number')
# else:
#     print("It is not an Armstrong number")

# this is for more than 3 digit digit
num = int(input("enter a number here: "))
order = len(str(num))

sum = 0
temp = num

while temp > 0:
    digit = temp%10
    sum += digit ** order
    temp //=10

if sum == num:
    print('It is an Armstrong Number')
else:
    print("It is not an Armstrong number")