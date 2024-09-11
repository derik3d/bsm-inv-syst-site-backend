from pymongo import MongoClient
from flask import jsonify
from bson.objectid import ObjectId


#MongoClient('mongodb://myuser:mypassword@localhost:27017/mydatabase')
client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase  # Create or connect to a database

# Collection (table equivalent in SQL)
collection = db.mycollection


# List all orders
def list_orders():
    documents = []
    # Retrieve all documents from the collection
    for document in collection.find():
        document['_id'] = str(document['_id'])  # Convert ObjectId to string
        documents.append(document)
    return jsonify(documents)

# Get a specific order by ID
def get_order(id):
    try:
        # Find the document by _id
        document = collection.find_one({"_id": ObjectId(id)})
        if document:
            document['_id'] = str(document['_id'])  # Convert ObjectId to string
            return jsonify(document), 200
        else:
            return jsonify({'error': 'Document not found'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Create a new order
def create_order(body):
    try:
        # Insert the document into the collection
        result = collection.insert_one(jsonify(body))
        return jsonify({'status': 'Document added', 'id': str(result.inserted_id)})
    except Exception as e:
        return jsonify({'error': str(e)})

# Update an existing order by ID
def update_order(id,body):
    try:
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": jsonify(body)})
        
        if result.matched_count == 0:
            return jsonify({'error': 'Document not found'})
        return jsonify({'status': 'Document updated'})
    except Exception as e:
        return jsonify({'error': str(e)})

# Delete an order by ID
def delete_order(id):
    try:
        # Delete the document from the collection
        result = collection.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count == 0:
            return jsonify({'error': 'Document not found'})
        return jsonify({'status': 'Document deleted'})
    except Exception as e:
        return jsonify({'error': str(e)})
