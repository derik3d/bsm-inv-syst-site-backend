""" routing file for flask """
from functools import wraps
from flask_cors import CORS

from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory

from controller.business_logic_mock import toy_business_logic_list_an_order


from controller.business_logic import list_products
from controller.business_logic import get_product
from controller.business_logic import create_product
from controller.business_logic import update_product
from controller.business_logic import delete_product

from controller.business_logic import list_orders
from controller.business_logic import get_order
from controller.business_logic import create_order
from controller.business_logic import update_order
from controller.business_logic import delete_order


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
_HELLO = "/hello"

_BY_ID = "/<id>"

_GENERAL_ROUTE = "/<path:path>"

###---------------------------------------------------------------------------------

@app.route(_PRODUCTS, methods=["GET"])
@api_key_required ## auth
def ep_list_products():
    """ list the current products """
    return list_products()

@app.route(_PRODUCTS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_product(id):
    """ show a product by id"""
    return get_product(id)

@app.route(_PRODUCTS, methods=["POST"])
@api_key_required ## auth
def ep_create_product():
    """ create a product with data"""
    return create_product(request.json)

@app.route(_PRODUCTS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_product(id):
    """ update a product with id and data"""
    return update_product(id, request.json)

@app.route(_PRODUCTS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_product(id):
    """ delete product by id"""
    return delete_product(id)

###---------------------------------------------------------------------------------


@app.route(_ORDERS, methods=["GET"])
@api_key_required ## auth
def ep_list_orders():
    """ list the current orders """
    return list_orders()

@app.route(_ORDERS+_BY_ID, methods=["GET"])
@api_key_required ## auth
def ep_get_order(id):
    """ show a order by id"""
    return get_order(id)

@app.route(_ORDERS, methods=["POST"])
@api_key_required ## auth
def ep_create_order():
    """ create a order with data"""
    return create_order(request.json)

@app.route(_ORDERS+_BY_ID, methods=["PUT"])
@api_key_required ## auth
def ep_update_order(id):
    """ update a order with id and data"""
    return update_order(id, request.json)

@app.route(_ORDERS+_BY_ID, methods=["DELETE"])
@api_key_required ## auth
def ep_delete_order(id):
    """ delete order by id"""
    return delete_order(id)

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
