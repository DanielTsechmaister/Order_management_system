from Product import Product


class Smartphone(Product):
    def __init__(self, product_id, product_type, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, product_type, brand, model, year, price)
        self.cell_net = self.fix_cell_net(cell_net)
        self.num_cores = self.fix_num_cores(num_cores)
        self.cam_res = self.fix_cam_res(cam_res)        #לבדוק אם הם רוצים שיהיה כתוב מגה פסקל או מספר שלם מספיק

    def fix_cell_net(self,cell_net):
        if type(cell_net) == str:
            if 'G' in cell_net:
                return cell_net
        return '4G'

    def fix_num_cores(self,num_cores):
        if type(num_cores) == int:
            return num_cores
        return 5

    def fix_cam_res(self,cam_res):
        if type(cam_res) == int:
            return cam_res
        return 4

    def print_me(self):
        super().print_me()
        print(f'Cell net:{self.cell_net}\nNum cores:{self.num_cores}\nCam res:{self.cam_res}')

    def __str__(self):
        sproduct = super().__str__()
        return f'{sproduct},{self.cell_net},{self.num_cores},{self.cam_res}'

    def __repr__(self):
        return str(self)

#
# s1=Smartphone(123,"AIR","appel","iphone",201,2000,6,"ss",'dd')
# s1.print_me()
# print(s1.__str__())
# print(s1.__repr__())