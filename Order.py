class Order:
    def __init__(self, order_id, client_id, product_id, quantity):
        self.order_id = order_id
        self.client_id = client_id
        self.product_id = product_id
        self.quantity = quantity


    def __str__(self):
        return f'{self.order_id}, {self.client_id}, {self.product_id}, {self.quantity}'





