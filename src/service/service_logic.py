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

    COLLECTION_NAME = "order"

    @staticmethod
    def list_orders():
        """ list"""
        return data_orders.list_general(OrderService.COLLECTION_NAME)

    @staticmethod
    def get_order(obj_id):
        """ get """
        return data_orders.get_general(OrderService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_order(body):
        """ create """
        return data_orders.create_general(OrderService.COLLECTION_NAME,body)

    @staticmethod
    def update_order(obj_id, body):
        """ update """
        return data_orders.update_general(OrderService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_order(obj_id):
        """ delete """
        return data_orders.delete_general(OrderService.COLLECTION_NAME,obj_id)

class StatusService:

    COLLECTION_NAME = "order"

    @staticmethod
    def list_orders():
        """ list"""
        return data_orders.list_general(StatusService.COLLECTION_NAME)

    @staticmethod
    def get_order(obj_id):
        """ get """
        return data_orders.get_general(StatusService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_order(body):
        """ create """
        return data_orders.create_general(StatusService.COLLECTION_NAME,body)

    @staticmethod
    def update_order(obj_id, body):
        """ update """
        return data_orders.update_general(StatusService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_order(obj_id):
        """ delete """
        return data_orders.delete_general(StatusService.COLLECTION_NAME,obj_id)


class InventoryItemService:

    COLLECTION_NAME = "order"

    @staticmethod
    def list_orders():
        """ list"""
        return data_orders.list_general(InventoryItemService.COLLECTION_NAME)

    @staticmethod
    def get_order(obj_id):
        """ get """
        return data_orders.get_general(InventoryItemService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_order(body):
        """ create """
        return data_orders.create_general(InventoryItemService.COLLECTION_NAME,body)

    @staticmethod
    def update_order(obj_id, body):
        """ update """
        return data_orders.update_general(InventoryItemService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_order(obj_id):
        """ delete """
        return data_orders.delete_general(InventoryItemService.COLLECTION_NAME,obj_id)

