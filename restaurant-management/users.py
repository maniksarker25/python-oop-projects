# Customer
# Employee
# Admin

from abc import ABC

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
     
class Employee(User):
    def __init__(self, name, email,phone, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# emp = Employee("rahim","rahim@gmail.com",932849234,"dhaka",23,"Chef",12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email,phone, address):
        super().__init__(name, phone, email, address)
        self.employees = [] # in memory database

    def add_empoloyee(self,name,email,phone,address,age,designation,salary):
        employee = Employee(name,email,phone,address,age,designation,salary) # employee class object
        self.employees.append(employee)
        print(f'{name} is added!!')

    def view_employee(self):
        print("Employee list:")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

ad = Admin("Admin","admin@gmail.com","93849384","Dhaka")
ad.add_empoloyee("Sagor","sagor@gmail.com","9834983","Khulna",34,"Chef",12000)

ad.view_employee()