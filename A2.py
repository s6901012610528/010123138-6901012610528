class Product:                                                      # Create class Product to represent a product
    def __init__(self, product_id, name, price, stock):             # Define attributes
        self.product_id = product_id                                # Define product ID variable
        self.name = name                                            # Define name variable
        self.price = price                                          # Define price variable
        self.stock = stock                                          # Define stock variable

    def display_info(self):                                         # Define display method
        print(f"Product ID : {self.product_id}")                    # Show product ID
        print(f"Product Name : {self.name}")                        # Show product name
        print(f"Price : {self.price} Baht")                         # Show price
        print(f"Stock : {self.stock} Item")                         # Show stock

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        print("\n===== Add Product =====")
        product_id = input("Product ID : ")
        name = input("Product Name : ")
        price = float(input("Price : "))
        stock = int(input("Stock : "))