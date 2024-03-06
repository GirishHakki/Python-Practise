# less than 30 uunits = 1 Rs
# between 31 to 50 uunits = 2 Rs
# more than 51 uunits = 3 Rs

units = int(input("Please Enter Units: "))

billAmount = 0

if units > 50:
    billAmount = (30*1) + (20 * 2) + ((units - 50)*3)
elif units > 30:
    billAmount = (30*1) + ((units - 30)*2)
else:
    billAmount = (units*1)

print("Bill Amount is Rs " + str(billAmount))