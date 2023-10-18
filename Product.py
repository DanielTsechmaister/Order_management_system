
class Product:
    def __init__(self, product_id, product_type, brand, model,year,price):
        self.product_id = int(product_id)
        self.product_type = product_type
        self.brand = brand
        self.model = model
        self.year = self.yearsfour(year)
        self.price = int(price)

    def yearsfour(self,year):
        if len(str(year)) == 4:
            return year
        return 2022

    def print_me(self):
        print(f'Product_id:{self.product_id}\nProduct_type:{self.product_type}\nBrand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self.price}')

    def __str__(self):
        return f'{self.product_id},{self.product_type},{self.brand},{self.model},{self.year},{self.price}'

    def __repr__(self):
        return str(self)

    def Is_popular(self):
        if int(self.year) > 2017 and int(self.price) < 3000:
            return True
        return False

# p1=Product(123,"AIR","appel","iphone",201,2000)
# p1.print_me()
# print(p1.__str__())
# print(p1.__repr__())
