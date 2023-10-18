from Client import Client
from Product import Product
from SuperStore import SuperStore
from Shirts import Shirts
from Order import Order
from ClientNotFoundError import ClientNotFoundError

import numpy as np
import matplotlib.pyplot as plt


orders = np.genfromtxt("orders.csv", delimiter=",", skip_header=1)
orders = orders.astype('int32')

store = SuperStore('products_supply.csv', 'clients.csv', 'shirts.csv', 'orders.csv')


#2
def get_payment(arr):
    list_shirt = store.list_shirts()
    prices = np.empty(len(arr))
    for i in range(len(arr)):
        product_id = arr[i, 2]
        for j in list_shirt:
            if str(product_id) == str(j.product_id):
                prices[i] = j.price * arr[i, 3]

    prices = prices.astype('int32')
    arr = np.column_stack((arr, prices))
    return  (arr)

#3
def most_expensiv(orders):
    order = get_payment(orders)
    maxi = order[:,4].max()
    max_order = order[order[:,4]==maxi]
    client_name = store.get_client(max_order[0,1]).name
    product_name = store.get_product(max_order[0,2]).product_name
    print(f'{max_order[0,0]}, {client_name},{product_name},{maxi}')

#4
def client_order(orders):
    client_id = int(input("Insert client id:"))
    order = get_payment(orders)
    if store.get_client(client_id) is None:
        raise ClientNotFoundError
    else:
        client_name = store.get_client(client_id).name
        a = np.count_nonzero(orders==client_id)
        b = order[order[:,1]==client_id]
        c = b[:,4].sum()
    print(f'Client name:{client_name}\nOrder quantity:{a}\nPayment:{c}')

#5
def over_average(orders):
    order = get_payment(orders)
    a = order[order[:,4]>=order[:,4].mean()]
    print(a)

#6
def dic_client(orders):
    dic = {}
    for row in orders:
        a = 0
        l_client = []
        client_id = row[1]
        for row in orders:
            if client_id == row[1]:
                a+=1
        l_client.append(a)
        dic[client_id] = l_client
    return dic

#7
def graph_bar(orders):
    data = dic_client(orders)
    client = np.array(list(data.keys()))
    client = [str(client_id) for client_id in client]
    sum_order = np.array(list(data.values()))
    sum_order = [int(order) for order in sum_order]
    plt.bar(client, sum_order, color='black')
    plt.xlabel('client')
    plt.ylabel('order')
    return plt.show()

#
if __name__ == '__main__':
    a = get_payment(orders)
    print(a)
    most_expensiv(orders)
    over_average(orders)
    print(dic_client(orders))
    graph_bar(orders)
    client_order(orders)

