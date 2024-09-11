# try except and finally

try:
    num1 = int(input("Enter a number num1\n"))
    num2 = int(input("Enter a number num2\n"))
    result = num1/num2

except ValueError as ve:
    print("Value Error, You have entered string instead of integer")

except ZeroDivisionError as zde:
    print("Zero Div. error, Don't use num2 as 0")

else:
    print(f"Result is {result}")

finally:
    print("This code always executed")


