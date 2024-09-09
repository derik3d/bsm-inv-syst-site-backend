import json

def toy_business_logic():
    """ mock util """
    return return_ok({
        "status" : "ok",
        "message" : "ok"
    })

def toy_business_logic_list_products():
    """ mock util """
    return return_ok({
        "status" : "ok",
        "message" : "list all products"
    })

def toy_business_logic_list_a_product():
    """ mock util """
    return return_ok({
        "status" : "ok",
        "message" : "list a product"
    })

def toy_business_logic_list_orders():
    """ mock util """
    return return_ok({
        "status" : "ok",
        "message" : "list all orders"
    })

def toy_business_logic_list_an_order():
    """ mock util """
    return return_ok({
        "status" : "ok",
        "message" : "list a order"
    })

def return_ok(response : str):
    """returns formatted answer"""

    return json.dumps(response), 200
