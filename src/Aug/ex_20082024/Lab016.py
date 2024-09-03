a = int(input("Enter the length of the first side\n"))
b = int(input("Enter the length of the second side\n"))
c = int(input("Enter the length of the third side\n"))
if a == b == c:
    print("The triangle is", "equilateral")
elif a == b or b == c or c == a:
    print("The triangle is", "isosceles")
else:
    print("The triangle is", "scalene")
