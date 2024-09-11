import json
import time
from pymongo import MongoClient
from bson import ObjectId

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['bigstoremanager']
inventory_collection = db['inventory_items']
orders_collection = db['orders']
status_updates_collection = db['status_updates']

# Clean up the collections before inserting new data
inventory_collection.delete_many({})
orders_collection.delete_many({})
status_updates_collection.delete_many({})

# Helper function to generate current timestamp
def current_timestamp():
    return time.time()

# SQL Products Data Mock
products = [
    {"id": 1, "product_name": "Smartphone", "product_description": "A high-end smartphone with advanced features."},
    {"id": 2, "product_name": "Big Dataphone", "product_description": "Old type dataphone."},
    {"id": 3, "product_name": "ID Card", "product_description": "A personalized ID card with unique identification."},
    {"id": 4, "product_name": "Credit Card", "product_description": "A personalized credit card."},
    {"id": 5, "product_name": "Business Checkbook", "product_description": "A checkbook for business transactions."},
    {"id": 6, "product_name": "Contract Web Document", "product_description": "A legally binding document signed online."},
    {"id": 7, "product_name": "Personal On-place Agreement", "product_description": "A contract signed personally."}
]

# Step 1: Create inventory items based on product data (at least two items per product)
inventory_items = []
for i, product in enumerate(products):
    for j in range(2):  # Create two inventory items for each product
        inventory_item = {
            "_id": ObjectId(),
            "creation": current_timestamp(),
            "product_id": product["id"],  # Reference product ID
            "product_name": product["product_name"],  # Reference product name
            "serial_number": f"SN{i+1}{j+1}",
            "additional_info": {"description": product["product_description"]},  # Include product description
            "order_info": None  # Initialize with no order info
        }
        inventory_items.append(inventory_item)

# Insert inventory items into the collection
inventory_collection.insert_many(inventory_items)

# Step 2: Create orders (3 single-item orders, 3 multi-item orders)
orders = []

# First group of 3 orders (each with 1 item)
for i in range(3):
    order = {
        "_id": ObjectId(),
        "creation": current_timestamp(),
        "updated": current_timestamp(),
        "status": None,
        "status_trace": [],
        "client": {
            "name": f"Client {chr(65 + i)}",
            "email": f"client{i+1}@example.com"
        },
        "inventory_items": [inventory_items[i]]  # 1 item per order
    }
    orders.append(order)

# Second group of 3 orders (each with 2 items)
for i in range(3, 6):
    order = {
        "_id": ObjectId(),
        "creation": current_timestamp(),
        "updated": current_timestamp(),
        "status": None,
        "status_trace": [],
        "client": {
            "name": f"Client {chr(65 + i)}",
            "email": f"client{i+1}@example.com"
        },
        "inventory_items": [inventory_items[i], inventory_items[i+7]]  # 2 items per order
    }
    orders.append(order)

# Insert orders into the collection
orders_collection.insert_many(orders)

# Step 3: Update statuses: first created, then pending, then delivered
status_updates = []

for order in orders:
    # Serialize the entire order object to JSON (including inventory_items)
    order_info = json.dumps(order, default=str)  # Dump the whole order object to JSON
    
    # "Created" status
    created_update = {
        "_id": ObjectId(),
        "creation": current_timestamp(),
        "status": "Created",
        "description": "Order has been created.",
        "order_info": order_info  # Storing dumped JSON of the entire order
    }
    status_updates.append(created_update)
    order["status"] = created_update
    order["status_trace"].append(created_update)

    # Update order_info for each inventory item in this order
    for item in order['inventory_items']:
        inventory_collection.update_one(
            {"_id": item['_id']},
            {"$set": {"order_info": order_info}}
        )

    # "Pending" status for some orders
    if order["client"]["name"] in ["Client D", "Client E", "Client F"]:
        pending_update = {
            "_id": ObjectId(),
            "creation": current_timestamp(),
            "status": "Pending",
            "description": "Order is pending.",
            "order_info": order_info  # Storing dumped JSON of the entire order
        }
        status_updates.append(pending_update)
        order["status"] = pending_update
        order["status_trace"].append(pending_update)

        # Update order_info for each inventory item in this order
        for item in order['inventory_items']:
            inventory_collection.update_one(
                {"_id": item['_id']},
                {"$set": {"order_info": order_info}}
            )

    # "Delivered" status for some orders
    if order["client"]["name"] in ["Client E", "Client F"]:
        delivered_update = {
            "_id": ObjectId(),
            "creation": current_timestamp(),
            "status": "Delivered",
            "description": "Order has been delivered.",
            "order_info": order_info  # Storing dumped JSON of the entire order
        }
        status_updates.append(delivered_update)
        order["status"] = delivered_update
        order["status_trace"].append(delivered_update)

        # Update order_info for each inventory item in this order
        for item in order['inventory_items']:
            inventory_collection.update_one(
                {"_id": item['_id']},
                {"$set": {"order_info": order_info}}
            )

# Insert status updates into the collection
status_updates_collection.insert_many(status_updates)

# Step 4: Update the orders with the status and status_trace
for order in orders:
    orders_collection.update_one(
        {"_id": order["_id"]},
        {"$set": {
            "status": order["status"],
            "status_trace": order["status_trace"],
            "updated": current_timestamp()
        }}
    )

print("Database cleaned and populated successfully with two inventory items per product and updated order_info!")
