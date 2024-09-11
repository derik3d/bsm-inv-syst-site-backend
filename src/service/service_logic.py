"""buisness logic -> before data manipulation"""

import dao.data_product as data_products
import dao.data_nosql_general as data_general


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

    COLLECTION_NAME = "orders"

    @staticmethod
    def list_orders():
        """ list"""
        return data_general.list_general(OrderService.COLLECTION_NAME)

    @staticmethod
    def get_order(obj_id):
        """ get """
        return data_general.get_general(OrderService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_order(body):
        """ create """
        return data_general.create_general(OrderService.COLLECTION_NAME,body)

    @staticmethod
    def update_order(obj_id, body):
        """ update """
        return data_general.update_general(OrderService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_order(obj_id):
        """ delete """
        return data_general.delete_general(OrderService.COLLECTION_NAME,obj_id)

class StatusUpdateService:

    COLLECTION_NAME = "status_updates"

    @staticmethod
    def list_statuss():
        """ list"""
        return data_general.list_general(StatusUpdateService.COLLECTION_NAME)

    @staticmethod
    def get_status(obj_id):
        """ get """
        return data_general.get_general(StatusUpdateService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_status(body):
        """ create """
        return data_general.create_general(StatusUpdateService.COLLECTION_NAME,body)

    @staticmethod
    def update_status(obj_id, body):
        """ update """
        return data_general.update_general(StatusUpdateService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_status(obj_id):
        """ delete """
        return data_general.delete_general(StatusUpdateService.COLLECTION_NAME,obj_id)


class InventoryItemService:

    COLLECTION_NAME = "inventory_items"

    @staticmethod
    def list_inventory_items():
        """ list"""
        return data_general.list_general(InventoryItemService.COLLECTION_NAME)

    @staticmethod
    def get_inventory_item(obj_id):
        """ get """
        return data_general.get_general(InventoryItemService.COLLECTION_NAME,obj_id)

    @staticmethod
    def create_inventory_item(body):
        """ create """
        return data_general.create_general(InventoryItemService.COLLECTION_NAME,body)

    @staticmethod
    def update_inventory_item(obj_id, body):
        """ update """
        return data_general.update_general(InventoryItemService.COLLECTION_NAME,obj_id, body)

    @staticmethod
    def delete_inventory_item(obj_id):
        """ delete """
        return data_general.delete_general(InventoryItemService.COLLECTION_NAME,obj_id)

