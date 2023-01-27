class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class POS:
    def __init__(self):
        self.products = {}
        self.total_amount = 0

    def add_product(self, product, quantity):
        if product.name in self.products:
            self.products[product.name]["quantity"] += quantity
        else:
            self.products[product.name] = {"product": product, "quantity": quantity}

    def remove_product(self, product_name, quantity):
        if product_name in self.products and self.products[product_name]["quantity"] >= quantity:
            self.products[product_name]["quantity"] -= quantity
        else:
            print("Invalid product or quantity.")

    def check_out(self):
        for product_name in self.products:
            product = self.products[product_name]["product"]
            quantity = self.products[product_name]["quantity"]
            self.total_amount += product.price * quantity
        print(f"Total amount:", self.total_amount)
        self.total_amount = 0
        self.products = {}

# Create some products
product1 = Product("Apple",  2)
product2 = Product("Orange", 1)
product3 = Product("Banana", 3)

# Initialize the POS system and add some products
pos = POS()
pos.add_product(product1, 11)
pos.add_product(product2, 10)
pos.add_product(product3, 15)

# Remove a product
pos.remove_product("Orange", 2)

# Check out
pos.check_out()
