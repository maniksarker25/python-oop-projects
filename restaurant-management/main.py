from food_item import FoodItem
from menu import Menu
from users import Customer,Admin,Employee
from restaurant import Restaurant
from orders import Order

mamar_restaurant = Restaurant("Mamar Restaurant")


def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter  you email: ")
    phone = input("Enter you phone num: ")
    address = input("Enter you address: ")

    customer = Customer(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter quantity: "))
            customer.add_to_cart(mamar_restaurant,item_name,item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.paybill()
        elif choice == 5:
            break
        else:
            print("Invalid choice!!")




def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter  you email: ")
    phone = input("Enter you phone num: ")
    address = input("Enter you address: ")

    admin = Admin(name=name,email=email,phone=phone,address=address)
    
    while True:
        print(f"Welcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
           item_name = input("Enter item name: ")
           item_price = input("Enter item price: ")
           item_quantity = int(input("Enter item quantity: "))
           item = FoodItem(item_name,item_price,item_quantity)
           admin.add_new_item(mamar_restaurant,item)
        elif choice == 2:
             name = input("Enter employee name: ")
             email = input("Enter employee email: ")
             phone = input("Enter employee Phone: ")
             designation = input("Enter employee designation: ")
             age = input("Enter employee age: ")
             salary = input("Enter employee salary: ")
             address = input("Enter employee address: ")
            
             admin.add_empoloyee(name, email,phone, address,age,designation,salary)

        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurant,item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice!!")