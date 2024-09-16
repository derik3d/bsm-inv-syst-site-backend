from pymongo import MongoClient
from flask import jsonify
from bson.objectid import ObjectId
import json

from model.orders.entity.status_update import StatusUpdate

# MongoClient('mongodb://myuser:mypassword@localhost:27017/mydatabase')
client = MongoClient("mongodb://localhost:27017/")
db = client.bigstoremanager  # Create or connect to a database

# Collection (table equivalent in SQL)


def convert_object_ids_to_str(document):
    """
    Recursively convert all ObjectId fields in the document to strings
    and change '_id' to 'id'.
    """
    if isinstance(document, dict):
        if "_id" in document and isinstance(document["_id"], ObjectId):
            # Rename '_id' to 'id' and convert ObjectId to string
            document["id"] = str(document.pop("_id"))

        # Recursively convert any nested dictionaries or lists
        for key, value in document.items():
            if isinstance(value, (dict, list)):
                convert_object_ids_to_str(value)

    elif isinstance(document, list):
        # If the document is a list, iterate through each item
        for index in range(len(document)):
            convert_object_ids_to_str(document[index])


# List all orders
def list_general(
    collection_name,
):
    collection = db[collection_name]
    documents = []
    try:
        # Retrieve all documents from the collection
        for document in collection.find():
            convert_object_ids_to_str(document)  # Convert ObjectId to string
            ##document = StatusUpdate(**document).model_dump()
            documents.append(document)
        return jsonify(documents)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


# Get a specific order by ID
def get_general(collection_name, obj_id):
    collection = db[collection_name]

    try:
        # Find the document by _id
        document = collection.find_one({"_id": ObjectId(obj_id)})

        if document:
            convert_object_ids_to_str(document)
            ##document = StatusUpdate(**document).model_dump()
            print(document)
            return document
        else:
            return jsonify({"error": "Document not found"})
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)})


# Create a new order
def create_general(collection_name, body):
    """deletes a document with a body"""
    collection = db[collection_name]
    try:
        model_dumo = body.model_dump()
        if 'id' in model_dumo:
            del model_dumo['id']
            
        print("TESSST")
        print(model_dumo)
        
        # Insert the document into the collection
        result = collection.insert_one(model_dumo)
        return jsonify({"status": "Document added", "id": str(result.inserted_id)})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


# Update an existing order by ID
def update_general(collection_name, obj_id, body):
    """updated a document with _id, and body"""
    collection = db[collection_name]
    
    model_dumo = body.model_dump()
    if 'id' in model_dumo:
        del model_dumo['id']

    try:
        result = collection.update_one(
            {"_id": ObjectId(obj_id)}, {"$set": model_dumo}
        )

        if result.matched_count == 0:
            return jsonify({"error": "Document not found"})
        return jsonify({"status": "Document updated"})
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)})


# Delete an order by ID
def delete_general(collection_name, obj_id):
    """deletes a document with _id"""
    collection = db[collection_name]
    try:
        # Delete the document from the collection
        result = collection.delete_one({"_id": ObjectId(obj_id)})

        if result.deleted_count == 0:
            return jsonify({"error": "Document not found"})
        return jsonify({"status": "Document deleted"})
    except Exception as e:
        print(str(e))
        return jsonify({"error": str(e)})
