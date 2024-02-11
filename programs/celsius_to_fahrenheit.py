# program to convert celsius to fahrenheit
# wkt the formula
# o degree = 32 fahrenheit
# (c *(9/5)) + 32 = f
# or
# (c *(1.8)) + 32 = f

celsius = int(input("enter temperature in celsius: "))
fahrenheit = (celsius*(9/5)) + 32
print("The converted value is", fahrenheit,"fahrenheit")