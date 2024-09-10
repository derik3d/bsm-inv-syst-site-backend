

import random
from pymongo import MongoClient
from flask import jsonify
from bson.objectid import ObjectId


#MongoClient('mongodb://myuser:mypassword@localhost:27017/mydatabase')
client = MongoClient('mongodb://localhost:27017/')
db = client.mydatabase  # Create or connect to a database

# Collection (table equivalent in SQL)
collection = db.mycollection

def get_all_documents():
    documents = []
    # Find all documents
    for document in collection.find():
        document['_id'] = str(document['_id'])  # Convert ObjectId to string
        documents.append(document)
    return jsonify(documents)

def add_document():
    #data = request.json  # Assume data is sent in JSON format
    # Insert the document into the collection
    result = collection.insert_one({
        "test":random.randint(0,9)
    })
    return jsonify({'status': 'Document added', 'id': str(result.inserted_id)})

def get_document(name):
    # Find the document by the name field
    print(name)
    document = collection.find_one({"test": 7})
    print(document)
    if document:
        document['_id'] = str(document['_id'])
        return jsonify(document)
    else:
        return jsonify({'error': 'Document not found'}), 404

def get_document_with_id(id):
    # Find the document by the name field
    print(id)
    document = collection.find_one({"_id": ObjectId(id)})
    if document:
        document['_id'] = str(document['_id'])
        return jsonify(document)
    else:
        return jsonify({'error': 'Document not found'}), 404

