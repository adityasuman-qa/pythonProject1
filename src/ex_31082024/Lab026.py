class Employee:
    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid


def walk(self):
    print("Walk")

def talk(self):
    print("Talk")

def print_details(self):
    print(self.name)
    print(self.age)
    print(self.phone)
    print(self.address)
    print(self.eid)
    print()


def get_employee_details(employee_number):
    print("Enter details of employee number")
    name = input("Name: ")
    age = int(input("Age: "))
    phone = input("Phone: ")
    address = input("Address: ")
    eid = input("Employee ID: ")
    return Employee(name, age, phone, address, eid)


employee1 = get_employee_details(1)
employee2 = get_employee_details(2)
print("Employee 1 Details\n:")
employee1.print_details()

print("Employee 2 Details:")
employee2.print_details()

employee1.walk()
employee2.talk()

# employee1 = Employee("Jon", 35, 9832543601, "1025-Charlton-Trace-Trce-Marietta-GA-30064", 340057)
print(employee1.name)

# employee2 = Employee("Isaac", 39, 8645543601, "1800-Little-Willeo-Rd-Marietta-GA-30068", 340089)
print(employee2.name)
