print("---Start of the program---")
try:
   a = int(input("Enter a num1\n"))
   b = int(input("Enter a num2\n"))
   c = a/b
   print("Result div is", c)

except Exception as e:
    print(e)
    print("Please check your input, it shouldn't be a string or zero")

print("---End of the program---")