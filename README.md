# SuperStore Project README

## Project Overview
The SuperStore project is a Python program that helps manage a supermarket selling a variety of products. The project consists of multiple files, each with its own class and functionality to handle different aspects of the store's operations. This README will provide an overview of each file and its associated classes and functions.

### Files and Classes

1. **Client**
   - Class: `Client`
   - Description: Represents a customer in the store.
   - Class Objects:
     - `client_id`: ID number of the client
     - `name`: Customer's name
     - `email`: Valid email address
     - `address`: Customer's address
     - `phone_number`: Customer's phone number (10 digits)
     - `gender`: Customer's gender (F/M)
   - Functions:
     - `mail()`: Validates and returns a valid email address.
     - `print_me()`: Prints client information.
     - `__str__()`: Converts the client object to a string representation.
     - `__repr__()`: Returns the string representation of the client.
   - Additional Class: `ClientNotFoundError` (exception class)

2. **Product**
   - Class: `Product`
   - Description: Represents a product in the store.
   - Class Objects:
     - `product_id`: ID number of the product (unique)
     - `product_type`: Type of product (smartphone, laptop, etc.)
     - `brand`: Company name of the product (Apple, Samsung, etc.)
     - `model`: Model of the product (iPhone, Galaxy, etc.)
     - `year`: Year of the product (4 digits)
     - `price`: Price of the product (in shekels)
   - Functions:
     - `yearsfour()`: Ensures that the year is represented by 4 digits.
     - `print_me()`: Prints product information.
     - `__str__()`: Converts the product object to a string representation.
     - `__repr__()`: Returns the string representation of the product.
     - `Is_popular()`: Checks if the product is popular based on criteria.
   
Laptop
   - Class: `Laptop` (Derived from `Product`)
   - Description: Represents a laptop in the store, inheriting from the Product class.
   - Additional Class Objects:
     - `CPU`: Processor name
     - `hard_disk`: Hard disk size (in gigabytes)
     - `screen`: Screen size (in inches)
   - Additional Functions: fix_CPU, fix_hard_disk, fix_screen

4. **Smartphone**
   - Class: `Smartphone` (Derived from `Product`)
   - Description: Represents a smartphone in the store, inheriting from the Product class.
   - Additional Class Objects:
     - `cell_net`: Supported cellular network
     - `num_cores`: Number of processor cores (an integer)
     - `cam_res`: Camera resolution (in megapixels)
   - Additional Functions: fix_cell_net, fix_num_cores, fix_cam_res

5. **Shirts**
   - Class: `Shirts` (Derived from `Product`)
   - Description: Represents various shirts in the store, inheriting from the Product class.
   - Additional Class Objects:
     - `product_name`: The name of the product
     - `units_in_stock`: Number of units of the product in the warehouse
   - Initialization of Brand, Model, and Year: "SuperStore," an empty string, and 2023, respectively

6. **Order**
   - Class: `Order`
   - Description: Represents an order for a product.
   - Class Objects:
     - `order_id`: ID number of the order
     - `client_id`: The client's number
     - `product_id`: The product number
     - `quantity`: Quantity ordered

7. **ShirtNotFoundError** and **ClientNotFoundError**
   - Exception classes to handle errors in the program and make code more readable.

8. **SuperStore**
   - Class: `SuperStore`
   - Description: Manages the product inventory in the store and customer information.
   - Functions:
     - Initialization: Reads data from CSV files to populate product and client lists.
     - `print_products()`: Prints the list of products in the store.
     - `get_product(product_id)`: Returns a product object by product ID.
     - `add_product(new_product)`: Adds a new product to the store.
     - `__iadd__(product)`: Overloaded method to add a product.
     - `remove_product(product_id)`: Removes a product from the store.
     - `get_all_by_brand(brand)`: Returns a list of products with a specific brand.
     - `get_all_by_price_under(price)`: Returns a list of products under a certain price.
     - `get_most_expensive_product()`: Returns the most expensive product in the store.
     - `print_clients()`: Prints the list of clients.
     - `get_client(client_id)`: Returns a client object by client ID.
     - `add_client(client)`: Adds a new client to the store.
     - `remove_client(client_id)`: Removes a client from the store.
     - `get_all_phones()`: Returns a list of smartphone products.
     - `get_all_laptop()`: Returns a list of laptop products.
     - `phone_average_price()`: Calculates the average price of smartphones.
     - `get_max_screen()`: Returns the largest screen size among laptops.
     - `get_common_cam()`: Returns the most common camera resolution among smartphones.
     - `list_popular()`: Returns a list of popular products.
     - `list_shirts()`: Returns a list of all shirts in the store.
     - `list_order()`: Prints all orders.
     - `get_shirt(product_id)`: Returns a shirt product by product ID.
     - `get_max_order_id()`: Returns the maximum order ID.
     - `add_order(client_id, product_id, quantity)`: Creates a new order in the store.

**Main Part Overview**
The main.py file is the entry point for your SuperStore program.
It allows users to interact with the program by providing a menu-driven interface. Users can perform various operations related to managing the store's products and customers.

*Menu Options*
The program provides the following menu options:
Of course, here is a more detailed breakdown of the main functions in the `main.py` file with the function name first:
   
   - `Print all products`: This option prints a list of all products currently available in the store.
   - `Print all clients`: It displays a list of all the store's customers.
   - `Add new product to the store`: Users can add a new product to the store by providing relevant details like product type, brand, model, year, and price.          Dependingon the product type (laptop or smartphone), additional attributes such as CPU, hard disk, screen size, cell network, number of cores, and camera resolution may be required.
   - `Add new client to the store`: This option allows users to add a new client to the store by providing details such as client ID, name, email, address, phone number, and gender.
   - `Remove product`: Users can remove a product from the store by entering the product's ID.
   - `Remove client`: This option allows users to remove a client from the store by providing the client's ID.
   - `Print all products under price`: Users can view a list of products in the store that are priced below a certain amount. The program prompts the user to enter a maximum price, and it displays the matching products.
   - `Print the most expensive product`: This option displays information about the most expensive product available in the store.
   - `Print smartphone list`: Users can view a list of all smartphone products in the store.
   - `Print laptop list`: This option displays a list of all laptop products available in the store.
   - `Print average phone price`: It calculates and prints the average price of all smartphone products.
   - `Print largest laptop screen`: Users can see the largest screen size among laptop products.
   - `Print common camera resolution`: This option identifies and prints the most common camera resolution among smartphone products in stock.
   - `Print popular products`: Users can view a list of popular products based on predefined criteria.
   - `Print all shirts`: It displays a list of all shirt products in the store.
   - `Create a new order`: Users can create a new order by providing details, including the client's ID, product ID, and quantity. The program checks for exceptions and handles them accordingly.
   - `Print all orders`: This option prints a list of all orders placed in the store.
   - `Exit`: Choosing this option exits the program.

  
This script provides an interactive interface for managing a store's products and clients through the `SuperStore` class and its associated methods.

**Input Validation**
The main part of the program includes input validation to ensure that users provide valid options within the specified range. If users enter invalid input, the program provides an error message and prompts them to enter a valid choice.
The program runs in a loop, continuously displaying the menu and processing user input until the user chooses to exit.

**Exception Handling**
The program includes error handling for potential exceptions, such as client or product not found, and provides meaningful error messages to guide the user and ensure the program continues to run smoothly.

This menu-driven approach allows for easy interaction with the SuperStore program, enabling users to perform various tasks related to product and customer management.



## The second part of the project consists of two different files that are used by the customers

1. **Super Store App (super_store_app.py):**

    - **Description:** The `super_store_app.py` file is a crucial part of the SuperStore project. It serves as the runtime file for the program, providing a graphical user interface for users to interact with the store's products and clients. This interface offers a user-friendly way to manage and display data from SuperStore.

    - **Features:**
      - *Display of Products:* Users can select a product type (All products, Laptops, Smartphones, or Shirts) from a dropdown list, and the app displays the selected products in a list.
      - *Creating a New Product:* The app allows users to create new products, specifically smartphones and laptops. It validates user input and provides feedback on the success or failure of the creation process.
   
    - *Usage:* The Super Store App simplifies the process of managing the store's products and clients. It enables users to view product lists and create new products efficiently.



2. **Shirt Orders Analysis (shirt_orders_analysis.py):**

    - **Description:** The `shirt_orders_analysis.py` module is a critical component of the SuperStore project that focuses on analyzing data related to shirt orders. It utilizes NumPy arrays and functions, as well as Matplotlib, to investigate and visualize data from various files. This module helps extract valuable insights from the store's order data.

    - **Features:**
      - **Data Loading and Analysis:** The module loads data from CSV files, such as orders.csv, shirts.csv, clients.csv, and products_supply.csv, into NumPy arrays. It performs data analysis based on specific requirements.
      - **Payment Calculation:** The module calculates payments for orders by multiplying the quantity of the order by the price of the product (shirt).
      - **Identifying the Most Expensive Order:** It identifies and prints the order number, customer name, product name, and payment for the most expensive order.
      - *Client Information Retrieval:* Users can input a customer's ID, and the module prints the customer's name, the number of orders they've made, and the total amount they've paid.
      - *Data Filtering:* The module can filter and print orders with payments above the average payment.
      - *Customer Order Analysis:* It builds a dictionary that contains the number of orders for each customer.
      - *Visualization:* The module creates a bar graph showing the number of orders per customer.

    - *Usage:* The Shirt Orders Analysis module empowers users to gain insights from the store's order data. It provides valuable information about payments, customer behavior, and order trends.
