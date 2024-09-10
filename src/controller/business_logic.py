"""buisness logic -> before data manipulation"""
import dao.data_product as data

from dao.data_order import get_all_documents

#PRODUCTS

def list_products():
    return data.list_products()

def get_product(id):
    return data.get_product(id)

def create_product(data):
    return data.create_product(data)

def update_product(id, data):
    return data.update_product(id, data)

def delete_product(id):
    return data.delete_product(id)

#ORDERS

def list_orders():
    return get_all_documents()