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
        print("\n===== Add Product =====")                          # Show menu title "Add Product"
        product_id = input("Product ID : ")                         # Input for product ID
        name = input("Product Name : ")                             # Input for product name
        price = float(input("Price : "))                            # Input for price
        stock = int(input("Stock : "))                              # Input for stock
        new_product = Product(product_id, name, price, stock)       # Create object new product
        self.products.append(new_product)                           # Add new product to array in class Inventory
        print("Product added successfully!")                        # Show "Product added successfully!"

    def show_product(self):                                         # Define method to show product
        print("\n===== All Product =====")                          # Show menu title "All Product"
        if(len(self.products) == 0):                                # Create condition if haven't Product
            print("No Product.")                                    # Show "No Product."
        else:                                                       # If have Product
            i = 0                                                   # Set i = 0 (index)
            while(i < len(self.products)):                          # Loop until i less number of products
                p = self.products[i]                                # Get first product from array
                print()                                             # Separator line
                p.display_info()                                    # Show product info
                print("------------------------")                   # Show separator line
                i = i + 1                                           # Increase index by 1

    def search_product(self):                                       # Define method to search product
        print("\n===== Search Product =====")                       # Show menu title "Search Product"
        search = input("Enter Product ID : ")                       # Input for product ID to search
        if(len(self.products) == 0):                                # Create condition if haven't Product
            print("No Product.")                                    # Show "No Product."
        else:                                                       # If have Product
            i = 0                                                   # Set i = 0 (index)
            while(i < len(self.products)):                          # Loop until i less number of products
                p = self.products[i]                                # Get first product from array
                if(p.product_id == search):                         # Create condition if product ID is equal to search ID
                    print("Product found!")                         # Show "Product found!"
                    print("------------------------")               # Show separator line
                    p.display_info()                                # Show product info
                    print("------------------------")               # Show separator line
                    return                                          # Exit method if found product
                i = i + 1                                           # Increase index by 1
            print("Product not found.")                             # Show "Product not found."

    def stock_in(self):                                             # Define method to receive stock
        print("\n===== Stock In =====")                             # Show menu title "Stock In"
        search = input("Enter Product ID : ")                       # Input for product ID to receive stock
        if(len(self.products) == 0):                                # Create condition if haven't Product
            print("No Product.")                                    # Show "No Product."
        else:                                                       # If have Product
            i = 0                                                   # Set i = 0 (index)
            while(i < len(self.products)):                          # Loop until i less number of products
                p = self.products[i]                                # Get first product from array
                if(p.product_id == search):                         # Create condition if product ID is equal to search ID
                    amount = int(input("Enter quantity : "))        # Input for quantity to receive stock
                    p.stock = p.stock + amount                      # Increase stock by amount
                    print("Stock in successful.")                   # Show "Stock in successful."
                    print(f"Remaining stock : {p.stock} units")     # Show remaining stock
                    return                                          # Exit method if found product
                i = i + 1                                           # Increase index by 1
                print("Product not found.")                         # Show "Product not found."

manager = Inventory()                                               # Create Inventory object name manager
while True:                                                         # Loop program until user exits
    print("\nInventory Management System Program")                  # Show title program
    print("====================================")                   # Show separator line
    print("Enter 1 : Add Product")                                  # Show main menu 1
    print("Enter 2 : Show all Product")                             # Show main menu 2
    print("Enter 3 : Search Product")                               # Show main menu 3
    print("Enter 4 : Stock In")                                     # Show main menu 4
    print("Enter 0 : Exit")                                         # Show main menu 0

    choice = int(input("Enter your choice : "))                     # Get user choice as integer
    if(choice == 1):                                                # Create condition choice 1
        manager.add_product()                                       # If select choice 1 to add product
    elif(choice == 2):                                              # Create condition choice 2
        manager.show_product()                                      # If select choice 2 to show all product
    elif(choice == 3):                                              # Create condition choice 3
        manager.search_product()                                    # If select choice 3 to search product
    elif(choice == 4):                                              # Create condition choice 4
        manager.stock_in()                                          # If select choice 4 to receive stock
    elif(choice == 0):                                              # Create condition choice 0
        break                                                       # If select choice 0 to exit program