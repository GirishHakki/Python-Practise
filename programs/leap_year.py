# program to check leap year

year = int(input("Enter the year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print(year, "its a leap year")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "its a leap year")

else:
    print(year, "not a leap year")