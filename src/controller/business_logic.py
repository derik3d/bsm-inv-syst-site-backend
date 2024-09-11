"""buisness logic -> before data manipulation"""

import dao.data_product as data_products
import dao.data_order as data_orders

#PRODUCTS

def list_products():
    return data_products.list_products()

def get_product(id):
    return data_products.get_product(id)

def create_product(body):
    return data_products.create_product(body)

def update_product(id, body):
    return data_products.update_product(id, body)

def delete_product(id):
    return data_products.delete_product(id)

#ORDERS

def list_orders():
    return data_orders.list_orders()

def get_order(id):
    return data_orders.get_order(id)

def create_order(body):
    return data_orders.create_order(body)

def update_order(id, body):
    return data_orders.update_order(id, body)

def delete_order(id):
    return data_orders.delete_order(id)
