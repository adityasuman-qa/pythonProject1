class Employee:

    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.address = input("Enter the address\n")
        self.eid = input("Enter the eid\n")

    def employee_details(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}", f"Address is {self.address}",
              f"eid is {self.eid}")

    def walk(self):
        print("Employee is walking")

    def talk(self):
        print("Employee is talking")
        print("Who is walking , E1")


employee1 = Employee()
employee2 = Employee()

employee1.employee_details()
employee2.employee_details()
employee1.walk()
employee2.walk()
employee1.talk()
employee2.talk()
