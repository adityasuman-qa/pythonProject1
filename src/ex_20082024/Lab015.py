year = int(input("Enter a year\n"))
if year / 4 and year == 0:
    print("Year is a leap year")
elif year / 100 and year == 0:
    print("Year is a leap year")
elif year / 400 and year == 0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")
