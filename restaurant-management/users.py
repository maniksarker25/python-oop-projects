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

class Customer:
    def __init__(self, name, email,phone, address):
        super().__init__(name, email, phone, address)
        self.cart = None
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
    
    def add_to_cart(self,restaurant,item_name):
        item = restaurant.menu.find_item(item_name)
        if item is not None:
            pass
        else:
            print("Item not found")

    def view_cart(self):
        print("***View Cart***")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f'{item.name} {item.price} {quantity}')
        print(f'Total price: {self.cart.total_price}')


class Order:
    def __init__(self):
        self.items = {} # order items database
    
    def add_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
        
    def remove(self,item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item.price * item.quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}
    
   
     
class Employee(User):
    def __init__(self, name, email,phone, address,age,designation,salary):
        super().__init__(name,email,phone, address)
        self.age = age
        self.designation = designation
        self.salary = salary


# emp = Employee("rahim","rahim@gmail.com",932849234,"dhaka",23,"Chef",12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, email,phone, address):
        super().__init__(name, phone, email, address)

    def add_empoloyee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
    
    def remove_item(self,restaurant,item):
        restaurant.remove_item(item)


class Restaurant:
    def __init__(self,name):
        self.name = name
        self.employees = [] # in memory database
        self.menu = FoodItem()

    def add_empoloyee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} is added!!')

    def view_employee(self):
        print("Employee list:")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

class Menu:
    def __init__(self):
        self.items = [] # items ar database

    def add_menu_item(self,item):
        self.items.append(item)

    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
            return None
    
    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"${item_name} deleted successfully from item menu!!")
        else:
            print("Item not found")

    def show_menu(self):
        print("**** MENU ITEMS *****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')


class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity





# mn = Menu()
# item = FoodItem("Pizza",12.45,10)
# mn.add_menu_item(item)
# mn.show_menu()

cm = Customer("Manik","manik@gmail.com",23232,"dhaka")
cm.view_menu()