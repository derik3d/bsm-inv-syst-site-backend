""" routing file for flask """
from functools import wraps
from flask_cors import CORS

from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory

from service.service_logic import ProductService
from service.service_logic import OrderService
from service.service_logic import StatusUpdateService
from service.service_logic import InventoryItemService

from model.products.entity.product import Product
from model.orders.entity.order import Order
from model.orders.entity.order import StatusUpdate
from model.orders.entity.order import InventoryItem


app = Flask(__name__)
CORS(app)


###################################################################

TEMPORARY_API_KEY = "xxxxxx"
def api_key_required(f):
    """ basic api key auth """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        #if api_key != TEMPORARY_API_KEY:
        #    return jsonify({'error': 'Unauthorized access >:('}), 403
        return f(*args, **kwargs)
    return decorated_function


####################################################################

API_URL = '/api_spec.yaml'  # Relative path to OpenAPI spec file

@app.route(API_URL)
def openapi_spec():
    """ return the openapi doc """
    return send_from_directory(".", "api_spec.yaml")


##########################################################################
_PRODUCTS = "/products"
_ORDERS = "/orders"
_STATUS = "/status"
_INVENTORYITEMS = "/inventory-items"
_HELLO = "/hello"

_BY_ID = "/<id>"

_GENERAL_ROUTE = "/<path:path>"

###--------------------------------------PRODUCT-------------------------------------------

@app.route(_PRODUCTS, methods=["GET"])
@api_key_required ## auth
def ep_list_products():
    """ list the current products """
    return ProductService.list_products()

@app.route(_PRODUCTS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_product(id):
    """ show a product by id"""
    return ProductService.get_product(id)

@app.route(_PRODUCTS, methods=["POST"])
@api_key_required ## auth
def ep_create_product():
    """ create a product with data"""
    product = Product(**request.json)
    return ProductService.create_product(product)

@app.route(_PRODUCTS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_product(id):
    """ update a product with id and data"""
    product = Product(**request.json)
    return ProductService.update_product(id, product)

@app.route(_PRODUCTS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_product(id):
    """ delete product by id"""
    return ProductService.delete_product(id)

###-----------------------------------------ORDER----------------------------------------


@app.route(_ORDERS, methods=["GET"])
@api_key_required ## auth
def ep_list_orders():
    """ list the current orders """
    return OrderService.list_orders()

@app.route(_ORDERS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_order(id):
    """ show a order by id"""
    return OrderService.get_order(id)

@app.route(_ORDERS, methods=["POST"])
@api_key_required ## auth
def ep_create_order():
    """ create a order with data"""
    order = Order(**request.json)
    return OrderService.create_order(order)

@app.route(_ORDERS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_order(id):
    """ update a order with id and data"""
    order = Order(**request.json)
    return OrderService.update_order(id, order)

@app.route(_ORDERS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_order(id):
    """ delete order by id"""
    return OrderService.delete_order(id)

###-----------------------------------------INVENTORYITEM----------------------------------------


@app.route(_INVENTORYITEMS, methods=["GET"])
@api_key_required ## auth
def ep_list_inventory_items():
    """ list the current inventory items """
    return InventoryItemService.list_inventory_items()

@app.route(_INVENTORYITEMS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_inventory_item(id):
    """ show a inventory item by id"""
    return InventoryItemService.get_inventory_item(id)

@app.route(_INVENTORYITEMS, methods=["POST"])
@api_key_required ## auth
def ep_create_inventory_item():
    """ create a inventory item with data"""
    inventory_item = InventoryItem(**request.json)
    return InventoryItemService.create_inventory_item(inventory_item)

@app.route(_INVENTORYITEMS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_inventory_item(id):
    """ update a inventory item with id and data"""
    inventory_item = InventoryItem(**request.json)
    return InventoryItemService.update_inventory_item(id, inventory_item)

@app.route(_INVENTORYITEMS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_inventory_item(id):
    """ delete inventory item by id"""
    return InventoryItemService.delete_inventory_item(id)

###-----------------------------------------STATUS----------------------------------------


@app.route(_STATUS, methods=["GET"])
@api_key_required ## auth
def ep_list_status():
    """ list the current statuss """
    return StatusUpdateService.list_statuss()

@app.route(_STATUS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_status(id):
    """ show a status by id"""
    return StatusUpdateService.get_status(id)

@app.route(_STATUS, methods=["POST"])
@api_key_required ## auth
def ep_create_status():
    """ create a status with data"""
    status = StatusUpdate(**request.json)
    return StatusUpdateService.create_status(status)

@app.route(_STATUS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_status(id):
    """ update a status with id and data"""
    status = StatusUpdate(**request.json)
    return StatusUpdateService.update_status(id, status)

@app.route(_STATUS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_status(id):
    """ delete status by id"""
    return StatusUpdateService.delete_status(id)

###---------------------------------------------------------------------------------

@app.route(_HELLO, methods=["GET", "POST"])
def hello():
    """ test hello endpoint """
    return "test hello" , 200

#####################################################################################3

# Catch-all route for undefined paths
@app.route(_GENERAL_ROUTE, methods=["GET", "POST"])
def catch_all(path):
    """fallback for an unmapped route"""
    return jsonify({
        "error": "Route not found",
        "path": path,
        "message": "This route does not exist. Redirecting you to a custom endpoint."
    }), 404

if __name__ == "__main__":
    app.run(debug=True)
