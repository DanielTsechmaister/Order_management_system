from Product import Product


class Laptop(Product):
    def __init__(self,product_id, product_type, brand, model, year, price, CPU, hard_disk, screen):
        super().__init__(product_id, product_type, brand, model, year, price)
        self.CPU = self.fix_CPU(CPU)
        self.hard_disk = self.fix_hard_disk(hard_disk)
        self.screen = self.fix_screen(screen)

    def fix_CPU(self,CPU):
        if type(CPU) == str:
            return CPU
        return 'Intel Core i5'

    def fix_hard_disk(self,hard_disk):
        if type(hard_disk) == int:
            return hard_disk
        return 256

    def fix_screen(self,screen):
        if type(screen) == int:
            return screen
        return 8

    def print_me(self):
        super().print_me()
        print(f'CPU:{self.CPU}')
        print(f'Hred disk:{self.hard_disk}')
        print(f'Screen:{self.screen}')

    def __str__(self):
        strproduct=super().__str__()
        return f'{strproduct},{self.CPU},{self.hard_disk},{self.screen}'

    def __repr__(self):
        return self.__str__()

#
# if __name__ == '__main__':
#     l1=Laptop(123,"AIR","appel","iphone", 201, 2000,'U','J','I')
#     l1.print_me()
#     print(l1.__str__())
#     print(l1.__repr__())