# Question no 1
class car:
    def __init__(self,brand:str,model:str,year:int,color:str):
        self.brand=brand
        self.model=model
        self.year=year
        self.color=color
    
    def display_info(self):
        print(f"car Information")
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"year:{self.year}")
        print(f"Color:{self.color}")

my_car=car("Honda","Civic",2023,"White")
my_car.display_info()

#Question no 2
class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, capacity_tons: float):
        super().__init__(brand, model, year)
        self.capacity_tons = capacity_tons

    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity_tons} tons")
my_truck = Truck("Toyota", "Revo", 2020, 10)
my_truck.display_info()
#Question no 3
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __len__(self):
        return self.pages
my_book = Book("OXFORD BOOK", "OXFORD UNIVERSITY", 320)

print(my_book)         
print(len(my_book))    
#Question no 4

class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, item_name, quantity=1):
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} x {item_name} to cart.")

    def remove_item(self, item_name, quantity=1):
        if item_name not in self.items:
            print(f"{item_name} is not in the cart.")
            return

        if quantity >= self.items[item_name]:
            del self.items[item_name]
            print(f"Removed all of {item_name} from cart.")
        else:
            self.items[item_name] -= quantity
            print(f"Removed {quantity} x {item_name} from cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item, qty in self.items.items():
                print(f" - {item}: {qty}")

    def clear_cart(self):
        self.items.clear()
        print("Cart has been cleared.")

    def __str__(self):
        return f"ShoppingCart({self.items})"
cart = ShoppingCart()

cart.add_item("Apple", 3)
cart.add_item("Banana", 2)
cart.view_cart()

cart.remove_item("Apple", 1)
cart.view_cart()

cart.remove_item("Banana", 2)
cart.view_cart()

cart.clear_cart()
cart.view_cart()

#question no 5

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Qty: {self.quantity})"
    
    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Updated quantity of {self.name} to {self.quantity}")


class Category:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print(f"Added {product.name} to category {self.name}")
    
    def list_products(self):
        print(f"Category: {self.name}")
        if not self.products:
            print("  No products in this category.")
        for product in self.products:
            print(f"  - {product}")

class Inventory:
    def __init__(self):
        self.categories = {}
    
    def add_category(self, category_name):
        if category_name not in self.categories:
            self.categories[category_name] = Category(category_name)
            print(f"Category '{category_name}' added.")
        else:
            print(f"Category '{category_name}' already exists.")
    
    def add_product(self, category_name, product):
        if category_name not in self.categories:
            print(f"Category '{category_name}' does not exist. Adding category first.")
            self.add_category(category_name)
        self.categories[category_name].add_product(product)
    
    def list_inventory(self):
        if not self.categories:
            print("Inventory is empty.")
            return
        for category in self.categories.values():
            category.list_products()


inventory = Inventory()

inventory.add_category("Electronics")
inventory.add_category("Groceries")

inventory.add_product("Electronics", Product("Laptop", 999, 10))
inventory.add_product("Electronics", Product("Smartphone", 599.20, 25))
inventory.add_product("Groceries", Product("Apple", 0.99, 100))
inventory.add_product("Groceries", Product("Milk", 2.99, 50))

inventory.list_inventory()
