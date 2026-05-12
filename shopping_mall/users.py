from abc import ABC

class User(ABC):
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
    

class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)


class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)