from menu import Menu
class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] # in memory database
        self.menu = Menu()

    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added!!')

    def view_employee(self):
        print("Employee list:")
        for emp in self.employees:
            print(f"Name\t Email\t Phone\ Address\t")
            print(emp.name, emp.email, emp.phone, emp.address)
