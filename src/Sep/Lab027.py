class Employee:
    def __init__(self, E1, E2):
        self.name = input("Enter the name of employee1\n")
        self.age = input("Enter the age of employee1\n")
        self.phone = input("Enter the phone number of employee1\n")
        self.address = input("Enter the address of employee1\n")
        self.eid = input("Enter the employee id of employee1\n")

        def __init__(self):
            self.name = input("Enter the name of employee2\n")
            self.age = input("Enter the age of employee2\n")
            self.phone = input("Enter the phone number of employee2\n")
            self.address = input("Enter the address of employee2\n")
            self.eid = input("Enter the employee id of employee2\n")

        def employee_details_display(self):
            print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}", f"Address is {self.address}",
                  f"eid is {self.eid}")


Employee1 = Employee()
Employee2 = Employee()

employee1.employee_details_display()
