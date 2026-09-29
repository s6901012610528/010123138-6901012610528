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

class Inventory:                                                    # Create class Inventory to manage products
    def __init__(self):                                             # Method runs when created object
        self.products = []                                          # Define empty array to store products

    def add_product(self):                                          # Define method to add product
        print("\n===== Add Product =====")                          # Show add Product
        product_id = input("Product ID : ")                         # Input for product ID
        name = input("Product Name : ")                             # Input for product name
        price = float(input("Price : "))                            # Input for price
        stock = int(input("Stock : "))                              # Input for stock
        