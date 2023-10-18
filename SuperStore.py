import csv
from Product import Product
from Client import Client
from Smartphone import Smartphone
from Laptop import Laptop
from Shirts import Shirts
from Order import Order
from ClientNotFoundError import ClientNotFoundError
from ShirtNotFoundError import ShirtNotFoundError


class SuperStore:
    def __init__(self, products_supply, clients, shirts, orders):
        self.product_list = []
        self.client_list = []
        self.orders = []
        with open(products_supply) as products_supply_file:
            products = csv.reader(products_supply_file)
            next(products_supply_file)
            for row in products:
                product_id = int(row[0])
                product_type = row[1]
                brand = row[2]
                model = row[3]
                year = row[4]
                price = float(row[5])
                CPU = row[6]
                hard_disk = row[7]
                screen = row[8]
                cell_net = row[9]
                num_cores = row[10]
                cam_res = row[11]
                if product_type == 'laptop':
                    product = Laptop(product_id, product_type, brand, model, year, price, CPU, int(hard_disk), int(screen))
                    self.product_list.append(product)
                elif product_type == 'smartphone':
                    product = Smartphone(product_id, product_type, brand, model, year, price, cell_net, int(num_cores), int(cam_res))
                    self.product_list.append(product)
                else:
                    print("is not product")
        with open(shirts) as shirts_file:
            read = csv.reader(shirts_file)
            next(read)
            for row in read:
                product_id = int(row[0])
                product_name = row[1]
                price = row[2]
                units_in_stock = row[3]
                product = Shirts(product_id, product_type, brand, model, year, price,product_name, int(units_in_stock))
                self.product_list.append(product)

        with open(clients) as clients_file:
            clients = csv.reader(clients_file)
            next(clients_file)
            for row in clients:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                c = Client(client_id,name,email,address,phone_number,gender)
                self.client_list.append(c)

        with open(orders) as orders_file:
            read = csv.reader(orders_file)
            next(read)
            for row in read:
                order_id = row[0]
                client_id = row[1]
                product_id = row[2]
                quantity = row[3]
                order = Order(order_id, client_id, product_id, quantity)
                self.orders.append(order)


    def print_products(self):
        for p in self.product_list:
            print(p)

    def get_product(self, product_id):
        for product in self.product_list:
            if product.product_id == product_id:
                return product
        return None

    def add_product(self, new_product):
        for product in self.product_list:
            if product.product_id == new_product.product_id:
                return False
        self.product_list.append(new_product)
        return True

    def __iadd__(self, product):
        for p in self.product_list:
            if p.product_id == product.product_id:
                return self
        self.product_list.append(product)
        return self

    def remove_product(self,product_id):
        for p in self.product_list:
            if p.product_id == product_id:
                self.product_list.remove(p)
                return True
        return False

    def get_all_by_brand(self,brand):
        list_brand=[]
        for p in self.product_list:
            if p.brand == brand:
                list_brand.append(p)
        return list_brand

    def get_all_by_price_under(self, price):
        list_price=[]
        for p in self.product_list:
            if p.price < price:
                list_price.append(p)
        return list_price

    def get_most_expensive_product(self):
        max_price = self.product_list[0]
        for p in self.product_list:
            if max_price.price <= p.price:
                max_price = p
        return max_price

    def print_clients(self):
        for c in self.client_list:
            print(c)


    def get_client(self, client_id):
        for client in self.client_list:
            if client.client_id == client_id:
                return client
        return None


    def add_client(self, c):
        for i in self.client_list:
            if c.client_id == i.client_id:
                return False
        self.client_list.append(c)
        return True

    def remove_client(self, client_id):
        for i in self.client_list:
            if i.client_id == client_id:
                self.client_list.remove(i)
                return True
        return False

    def get_all_phones(self):
        all_phones=[]
        for product in self.product_list:
            if type(product) == Smartphone:
                all_phones.append(product)
        return all_phones

    def get_all_laptop(self):
        all_laptop=[]
        for product in self.product_list:
            if type(product) == Laptop:
                all_laptop.append(product)
        return all_laptop

    def phone_average_price(self):
        sum1 = 0
        n = 0
        for product in self.product_list:
            if type(product) == Smartphone:
                sum1 += product.price
                n += 1
        return sum1/n


    def get_max_screen(self):
        max_s = 0
        for product in self.get_all_laptop():
            if int(product.screen) > max_s:
                max_s = int(product.screen)
        return max_s

    def get_common_cam(self):
        res_cam = []
        for product in self.product_list:
            if type(product) == Smartphone:
                res_cam.append(product.cam_res)
        most_common = max(set(res_cam), key=res_cam.count)
        return most_common


    def list_popular(self):
        popular = []
        for product in self.product_list:
            pop = Product.Is_popular(product)
            if pop == True:
                popular.append(product)
        return popular

    def list_shirts(self):
        list_shirt = []
        for product in self.product_list:
            if type(product) == Shirts:
                list_shirt.append(product)
        return list_shirt

    def list_order(self):
        for order in self.orders:
            print(order)

    def get_shirt(self, product_id):
        for product in self.list_shirts():
            if product.product_id == product_id:
                return product
        return None

    def get_max_order_id(self):
        max_id = 0
        for order in self.orders:
            if int(order.order_id) > max_id:
                max_id = int(order.order_id)
        return max_id


    def add_order(self, client_id, product_id, quantity):
        if self.get_client(client_id) is None:
            raise ClientNotFoundError(f'Clint not found with ID')
        product = self.get_product(product_id)
        if self.get_product(product_id) is None:
            raise ShirtNotFoundError(f'Shirt not found with ID ')
        if self.get_product(product_id) is not None:
            if type(product) == Shirts and quantity > product.units_in_stock:
                raise ValueError(f'The quantity is too large')
            if type(product) != Shirts:
                quantity = 1

        order_id = int(self.get_max_order_id()) + 1
        new_order = Order(order_id, client_id, product_id, quantity)
        self.orders.append(new_order)




if __name__ == '__main__':
    store = SuperStore('products_supply.csv', 'clients.csv', 'shirts.csv', 'orders.csv')
    client_id = 98699
    product_id = 45
    quantity = 2
    new_order = store.add_order(client_id, product_id, quantity)
    print('The order successfully added.')

    y=store.get_max_screen()
    print(y)
#
