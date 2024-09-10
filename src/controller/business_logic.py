
from dao.data_product import index
from dao.data_order import get_all_documents

def list_products():
    return index()

def list_orders():
    return get_all_documents()