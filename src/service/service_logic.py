"""buisness logic -> before data manipulation"""

import dao.data_product as data_products
import dao.data_order as data_orders


#PRODUCTS
class ProductService:

    @staticmethod
    def list_products():
        """crud product """
        return data_products.list_products()

    @staticmethod
    def get_product(id):
        """crud product """
        return data_products.get_product(id)

    @staticmethod
    def create_product(body):
        """crud product """
        return data_products.create_product(body)

    @staticmethod
    def update_product(id, body):
        """crud product """
        return data_products.update_product(id, body)

    @staticmethod
    def delete_product(id):
        """crud product """
        return data_products.delete_product(id)

#ORDERS
class OrderService:

    @staticmethod
    def list_orders():
        """crud order """
        return data_orders.list_orders()

    @staticmethod
    def get_order(id):
        """crud order """
        return data_orders.get_order(id)

    @staticmethod
    def create_order(body):
        """crud order """
        return data_orders.create_order(body)

    @staticmethod
    def update_order(id, body):
        """crud order """
        return data_orders.update_order(id, body)

    @staticmethod
    def delete_order(id):
        """crud order """
        return data_orders.delete_order(id)
