class Employee:
    def __init__(self, id, name, hourly_rate):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_pay()
        return total_payroll

# example usage
payroll = Payroll()

while True:
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Calculate payroll")
    print("4. Quit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        hourly_rate = float(input("Enter employee hourly rate: "))
        employee = Employee(id, name, hourly_rate)
        payroll.add_employee(employee)
    elif choice == 2:
        id = int(input("Enter employee ID: "))
        for employee in payroll.employees:
            if employee.id == id:
                payroll.remove_employee(employee)
                break
        else:
            print("Employee not found.")
    elif choice == 3:
        print("Total payroll:", payroll.calculate_total_payroll())
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
class Employee:
    def __init__(self, id, name, hourly_rate):
        self.id = id
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_pay()
        return total_payroll

# example usage
payroll = Payroll()

while True:
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Calculate payroll")
    print("4. Quit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        hourly_rate = float(input("Enter employee hourly rate: "))
        employee = Employee(id, name, hourly_rate)
        payroll.add_employee(employee)
    elif choice == 2:
        id = int(input("Enter employee ID: "))
        for employee in payroll.employees:
            if employee.id == id:
                payroll.remove_employee(employee)
                break
        else:
            print("Employee not found.")
    elif choice == 3:
        print("Total payroll:", payroll.calculate_total_payroll())
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
