#  Break - Based on condition , exit the loop
for i in range(0, 10, 1):  # 0 to 9 , start
    print(i)


# range(0, 10, 1)
#range(0, 10)
#range(10)

#  Break - Based on condition , exit the loop
for i in range(0, 10, 1):
    if i == 6:
        print(i)
    else:
        print("No O/P")


# | i  | Condition | O/P
# | 0  | 0 == 6 -> False | O/P -> No O/P
# | 1  | 1 == 6 -> False | O/P -> No O/P
# | 2  | 2 == 6 -> False | O/P -> No O/P
# | 3  | 3 == 6 -> False | O/P -> No O/P
# | 4  | 4 == 6 -> False | O/P -> No O/P
# | 5  | 5 == 6 -> False | O/P -> No O/P
# | 6  | 5 == 6 -> True | O/P -> 6
# | 7  | 7 == 6 -> False | O/P -> No O/P
# | 8  | 8 == 6 -> False | O/P -> No O/P
# | 9  | 9 == 6 -> False | O/P -> No O/P


#  Break - Based on condition , exit the loop
for i in range(0, 10, 1):
    if i == 6 or i == 5:
        print(i)
    else:
        pass # pass it is used to pass


# | i  | Condition | O/P
# | 0  | 0 == 6 -> False | O/P -> No O/P
# | 1  | 1 == 6 -> False | O/P -> No O/P
# | 2  | 2 == 6 -> False | O/P -> No O/P
# | 3  | 3 == 6 -> False | O/P -> No O/P
# | 4  | 4 == 6 -> False | O/P -> No O/P
# | 5  | 5 == 6 -> False | O/P -> No O/P
# | 6  | 5 == 6 -> True | O/P -> 6
# | 7  | 7 == 6 -> False | O/P -> No O/P
# | 8  | 8 == 6 -> False | O/P -> No O/P
# | 9  | 9 == 6 -> False | O/P -> No O/P

for i in range(0, 100):
    if i % 2 == 0:
        print(i)
    else:
        pass

# | i  | Condition | O/P
# | 0  | 0%2 == 0 - True | O/P -> 0
# | 1  | 1%2 == 0 - False | O/P -> Not Out Put


# Continue Statement
# continue statement skips the current iteration of a loop and
# moves to the next iteration.

for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)

# | i  | Condition | O/P
# | 0  | 0%2 == 0 -> True | continue - skip No O/P
# | 1  | 1%2 == 0 -> False | 1
# | 2  | 1%2 == 0 -> True | continue - skip No O/P
# | 3  | 3%2 == 0 -> False | 3


# pass - can be used in the statment, fucntions, class and obejcts