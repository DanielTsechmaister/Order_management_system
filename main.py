from Client import Client
from Product import Product
from SuperStore import SuperStore
from Laptop import Laptop
from Smartphone import Smartphone
from Shirts import Shirts
from Order import Order



menu = [
    "1. Print all products",
    "2. Print all clients",
    "3. Add new product to the store",
    "4. Add new client to the store",
    "5. Remove product",
    "6. Remove client",
    "7. Print all products under price",
    "8. Print the most expensive product",
    "9.Print smartphone list",
    "10.Print laptop list",
    "11.Print average phone price",
    "12.Print largest laptop screen",
    "13.Print common camera resolution",
    "14.Print popular product",
    "15.Print all shirts",
    "16.Create a new order",
    "17.Print all orders",
    "18.EXIT",
]


def display_menu():
    print()
    print("--- MENU ---")
    for item in menu:
        print(item)


def is_valid_input(i):
    return i.isdigit() and 1 <= int(i) <= len(menu)


def print_all_products(store):
    store.print_products()


def print_all_clients(store):
    store.print_clients()

def add_new_product(store):
    pid = int(input("Insert product id: "))
    product_type = input("Insert product type: ")
    brand = input("Insert product brand: ")
    model = input("Insert product model: ")
    year = int(input("Insert product year: "))
    price = float(input("insert product price: "))
    if product_type == 'laptop':
        CPU = input("insert product CPU: ")
        hard_disk = int(input("insert product hard_disk: "))
        screen = int(input("insert product screen: "))
        new_product = Laptop(pid, product_type, brand, model, year, price, CPU, hard_disk, screen)
        store.add_product(new_product)
    elif product_type == 'smartphone':
        cell_net = input("insert product cell_net: ")
        num_cores = int(input("insert product num_cores: "))
        cam_res = int(input("insert product cam_res: "))
        new_product = Smartphone(pid, product_type, brand, model, year, price, cell_net, num_cores, cam_res)
        store += new_product
    elif type != "laptop" and type!="smartphone":
        print("You choose type: laptop or smartphone")



def add_new_client(store):
    cid = int(input("insert client id: "))
    name = input("insert client name: ")
    email = input("insert product email: ")
    address = input("insert product address: ")
    phone_number = input("insert product phone number: ")
    gender = input("insert gender (M/F): ")

    new_client = Client(cid, name, email, address, phone_number, gender)
    store.add_client(new_client)


def remove_product(store):
    pid = int(input("insert product id: "))

    if store.remove_product(pid):
        print(f"{pid} deleted!")
    else:
        print(f"{pid} not exist!")


def remove_client(store):
    cid = int(input("insert client id: "))
    if store.remove_client(cid):
        print(f"{cid} deleted!")
    else:
        print(f"{cid} not exist!")


def print_all_products_above_price(store):
    price = float(input("insert a maximum price: "))
    product_list = store.get_all_by_price_under(price)
    print(f"---- All products under price ({price}): ")
    for p in product_list:
        print(p)


def print_most_expensive_product(store):
    most_expensive = store.get_most_expensive_product()
    print(f"The most expensive product is: {most_expensive}")


def get_all_phones(store):
    all_phones = store.get_all_phones()
    print(f"All phones: {all_phones}")


def get_all_laptop(store):
    all_laptop = store.get_all_laptop()
    print(f"All laptop: {all_laptop}")


def phone_average_price(store):
    average_price = store.phone_average_price()
    print(f'The average price: {average_price}')


def get_max_screen(store):
    max_screen = store.get_max_screen()
    print(f"The max screen is:{max_screen}")


def get_common_cam(store):
    camres1 = store.get_common_cam()
    print(f'The common cam: {camres1}')


def list_popular(store):
    listpopular = store.list_popular()
    print(f'The popular list:{listpopular}')

def list_shirts(store):
    l_shirts = store.list_shirts()
    print(f'All shirts: {l_shirts}')

def Create_order(store):
    try:
        client_id = int(input(f'Insert client id:'))
        product_id = int(input(f'Insert product id:'))
        quantity = int(input(f'Insert how:'))
        store.add_order(client_id, product_id, quantity)
    except Exception as e:
        print(e)


def list_order(store):
    store.list_order()


def get_valid_user_choice():
    user_input = input("What is your choice? ")

    while not is_valid_input(user_input):
        print(f"Invalid input! Please choose number option from the menu: {1} - {len(menu)}")
        user_input = input("What is your choice? ")

    return int(user_input)


def main():
    store = SuperStore('products_supply.csv', 'clients.csv', 'shirts.csv', 'orders.csv')
    user_choice = -1

    while user_choice < 18:
        display_menu()
        user_choice = get_valid_user_choice()

        if user_choice == 1:
            print_all_products(store)
        if user_choice == 2:
            print_all_clients(store)
        if user_choice == 3:
            add_new_product(store)
        if user_choice == 4:
            add_new_client(store)
        if user_choice == 5:
            remove_product(store)
        if user_choice == 6:
            remove_client(store)
        if user_choice == 7:
            print_all_products_above_price(store)
        if user_choice == 8:
            print_most_expensive_product(store)
        if user_choice == 9:
            get_all_phones(store)
        if user_choice == 10:
            get_all_laptop(store)
        if user_choice == 11:
            phone_average_price(store)
        if user_choice == 12:
            get_max_screen(store)
        if user_choice == 13:
            get_common_cam(store)
        if user_choice == 14:
            list_popular(store)
        if user_choice == 15:
            list_shirts(store)
        if user_choice == 16:
            Create_order(store)
        if user_choice == 17:
            list_order(store)


    print("Bye Bye!")


if __name__ == '__main__':
    main()

