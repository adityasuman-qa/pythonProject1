# Taking inputs from the user
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
sum_result = num1 + num2
pow_result = num1** num2
subst_result = num1-num2
mul_result = num1*num2
div_result = num1/num2
# Formatting the output using f-string
print(f"The sum of {num1} and {num2} is {sum_result}.")
print(f"The pow of {num1} and {num2} is {pow_result}.")
print(f"The subst of {num1} and {num2} is {subst_result}.")
print(f"The mul of {num1} and {num2} is {mul_result}.")
print(f"The div of {num1} and {num2} is {div_result}.")