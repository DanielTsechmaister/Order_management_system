from Product import Product


class Shirts(Product):
    def __init__(self, product_id, product_type, brand, model, year, price, product_name, units_in_stock):
        super().__init__(product_id, product_type, brand, model, year, price)
        self.product_type = "shirt"
        self.brand = "SuperStore"
        self.model = ""
        self.year = 2023
        self.product_name = product_name
        self.units_in_stock = units_in_stock

    def __str__(self):
        return f'{self.product_id},{self.product_name},{self.price},{self.units_in_stock}'
