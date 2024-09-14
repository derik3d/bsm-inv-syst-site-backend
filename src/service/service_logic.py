"""buisness logic -> before data manipulation"""

import dao.data_product as crud_sql
import dao.data_nosql_general as crud_nosql


# PRODUCTTYPES
class ProductTypeService:

    TABLE_NAME = "product_type"

    @staticmethod
    def list_product_types():
        """crud product type"""
        return crud_sql.list_general(ProductTypeService.TABLE_NAME)

    @staticmethod
    def get_product_type(object_id):
        """crud product type"""
        return crud_sql.get_general(ProductTypeService.TABLE_NAME, object_id)

    @staticmethod
    def create_product_type(body):
        """crud product_type"""
        return crud_sql.create_general(ProductTypeService.TABLE_NAME, body)

    @staticmethod
    def update_product_type(object_id, body):
        """crud product_type"""
        return crud_sql.update_general(ProductTypeService.TABLE_NAME, object_id, body)

    @staticmethod
    def delete_product_type(object_id):
        """crud product_type"""
        return crud_sql.delete_general(ProductTypeService.TABLE_NAME, object_id)


# PRODUCTS
class ProductService:

    TABLE_NAME = "product"

    @staticmethod
    def list_products():
        """crud product"""
        return crud_sql.list_general(ProductService.TABLE_NAME)

    @staticmethod
    def get_product(object_id):
        """crud product"""
        return crud_sql.get_general(ProductService.TABLE_NAME, object_id)

    @staticmethod
    def create_product(body):
        """crud product"""
        return crud_sql.create_general(ProductService.TABLE_NAME, body)

    @staticmethod
    def update_product(object_id, body):
        """crud product"""
        return crud_sql.update_general(ProductService.TABLE_NAME, object_id, body)

    @staticmethod
    def delete_product(object_id):
        """crud product"""
        return crud_sql.delete_general(ProductService.TABLE_NAME, object_id)


# ORDERS
class OrderService:
    """logic class for orders """

    COLLECTION_NAME = "orders"

    @staticmethod
    def list_orders():
        """list"""
        return crud_nosql.list_general(OrderService.COLLECTION_NAME)

    @staticmethod
    def get_order(obj_id):
        """get"""
        return crud_nosql.get_general(OrderService.COLLECTION_NAME, obj_id)

    @staticmethod
    def create_order(body):
        """create"""
        return crud_nosql.create_general(OrderService.COLLECTION_NAME, body)

    @staticmethod
    def update_order(obj_id, body):
        """update"""
        return crud_nosql.update_general(OrderService.COLLECTION_NAME, obj_id, body)

    @staticmethod
    def delete_order(obj_id):
        """delete"""
        return crud_nosql.delete_general(OrderService.COLLECTION_NAME, obj_id)


class StatusUpdateService:
    """logic class for status """

    COLLECTION_NAME = "status_updates"

    @staticmethod
    def list_statuss():
        """list"""
        return crud_nosql.list_general(StatusUpdateService.COLLECTION_NAME)

    @staticmethod
    def get_status(obj_id):
        """get"""
        return crud_nosql.get_general(StatusUpdateService.COLLECTION_NAME, obj_id)

    @staticmethod
    def create_status(body):
        """create"""
        return crud_nosql.create_general(StatusUpdateService.COLLECTION_NAME, body)

    @staticmethod
    def update_status(obj_id, body):
        """update"""
        return crud_nosql.update_general(
            StatusUpdateService.COLLECTION_NAME, obj_id, body
        )

    @staticmethod
    def delete_status(obj_id):
        """delete"""
        return crud_nosql.delete_general(StatusUpdateService.COLLECTION_NAME, obj_id)


class InventoryItemService:
    """logic class for inventory item """

    COLLECTION_NAME = "inventory_items"

    @staticmethod
    def list_inventory_items():
        """list"""
        return crud_nosql.list_general(InventoryItemService.COLLECTION_NAME)

    @staticmethod
    def get_inventory_item(obj_id):
        """get"""
        return crud_nosql.get_general(InventoryItemService.COLLECTION_NAME, obj_id)

    @staticmethod
    def create_inventory_item(body):
        """create"""
        return crud_nosql.create_general(InventoryItemService.COLLECTION_NAME, body)

    @staticmethod
    def update_inventory_item(obj_id, body):
        """update"""
        return crud_nosql.update_general(
            InventoryItemService.COLLECTION_NAME, obj_id, body
        )

    @staticmethod
    def delete_inventory_item(obj_id):
        """delete"""
        return crud_nosql.delete_general(InventoryItemService.COLLECTION_NAME, obj_id)
