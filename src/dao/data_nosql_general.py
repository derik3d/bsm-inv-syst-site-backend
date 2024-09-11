from pymongo import MongoClient
from flask import jsonify
from bson.objectid import ObjectId




#MongoClient('mongodb://myuser:mypassword@localhost:27017/mydatabase')
client = MongoClient('mongodb://localhost:27017/')
db = client.bigstoremanager  # Create or connect to a database

# Collection (table equivalent in SQL)


def convert_object_ids_to_str(document):
    """
    Recursively convert all ObjectId fields in the document to strings.
    """
    if isinstance(document, dict):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)
            elif isinstance(value, dict) or isinstance(value, list):
                convert_object_ids_to_str(value)
    elif isinstance(document, list):
        for index in range(len(document)):
            convert_object_ids_to_str(document[index])


# List all orders
def list_general(collection_name,):
    collection = db[collection_name]
    documents = []
    # Retrieve all documents from the collection
    for document in collection.find():
        convert_object_ids_to_str(document)  # Convert ObjectId to string
        documents.append(document)

    return jsonify(documents)

# Get a specific order by ID
def get_general(collection_name,obj_id):
    collection = db[collection_name]

    print(id)

    try:
        # Find the document by _id
        document = collection.find_one({"_id": ObjectId(obj_id)})
        print((document))

        if document:
            convert_object_ids_to_str(document)
            return document
        else:
            return jsonify({'error': 'Document not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Create a new order
def create_general(collection_name,body):
    """deletes a document with a body"""
    collection = db[collection_name]
    try:
        # Insert the document into the collection
        result = collection.insert_one(jsonify(body))
        return jsonify({'status': 'Document added', 'id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'error': str(e)})

# Update an existing order by ID
def update_general(collection_name,obj_id,body):
    """updated a document with _id, and body"""
    collection = db[collection_name]
    try:
        result = collection.update_one({"_id": ObjectId(obj_id)}, {"$set": jsonify(body)})
        
        if result.matched_count == 0:
            return jsonify({'error': 'Document not found'})
        return jsonify({'status': 'Document updated'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Delete an order by ID
def delete_general(collection_name,obj_id):
    """deletes a document with _id"""
    collection = db[collection_name]
    try:
        # Delete the document from the collection
        result = collection.delete_one({"_id": ObjectId(obj_id)})
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Document not found'})
        return jsonify({'status': 'Document deleted'})
    except Exception as e:
        return jsonify({'error': str(e)})
