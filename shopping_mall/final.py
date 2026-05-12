
# E-Commerce App using OOP

class User:
    def __init__(self, email, password):
        self.email = email
        self._password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.orders = []

    def place_order(self, product, quantity):
        if product.stock >= quantity:
            total_price = product.price * quantity

            order = Order(self, product, quantity, total_price)
            self.orders.append(order)

            product.stock -= quantity

            print(f"\nOrder placed successfully!")
            print(f"Product: {product.name}")
            print(f"Quantity: {quantity}")
            print(f"Total Price: ${total_price}")

        else:
            print("Not enough stock available!")


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def publish_product(self, store, name, price, stock):
        product = Product(name, price, stock, self)

        self.products.append(product)
        store.add_product(product)

        print(f"{name} added successfully!")


class Product:
    def __init__(self, name, price, stock, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller

    def __repr__(self):
        return f"{self.name} - ${self.price} - Stock: {self.stock}"


class Order:
    def __init__(self, customer, product, quantity, total_price):
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_price = total_price


class ECommerceStore:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    # Customer Registration
    def register_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)

        print("Customer account created successfully!")
        return customer

    # Seller Registration
    def register_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)

        print("Seller account created successfully!")
        return seller

    # Add Product
    def add_product(self, product):
        self.products.append(product)

    # Show Available Products
    def show_products(self):
        print("\nAvailable Products:")

        available = False

        for index, product in enumerate(self.products, start=1):

            # Hide stock out products
            if product.stock > 0:
                available = True
                print(
                    f"{index}. {product.name} | Price: ${product.price} | Stock: {product.stock}"
                )

        if not available:
            print("No products available!")


# =========================
# Main Program
# =========================

store = ECommerceStore()

# Create Seller
seller1 = store.register_seller("seller@gmail.com", "1234")

# Seller publishes products
seller1.publish_product(store, "Laptop", 1200, 5)
seller1.publish_product(store, "Mouse", 25, 10)
seller1.publish_product(store, "Keyboard", 50, 0)

# Create Customer
customer1 = store.register_customer("customer@gmail.com", "abcd")

# Show products
store.show_products()

# Customer places order
customer1.place_order(store.products[0], 2)

# Show updated products
store.show_products()