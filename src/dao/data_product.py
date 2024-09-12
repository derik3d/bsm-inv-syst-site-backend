from flask import  jsonify
import mysql.connector

# MySQL connection setup
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'bigstoremanager'
}

def get_db_connection():
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection

def list_general(table):
    query = "SELECT * FROM " + table
    products=execute_query(query, fetch=2)
    return products

def get_general(table,id):
    query = 'SELECT * FROM '+ table + ' WHERE id = %s'
    values = (id,)
    product = execute_query(query,values, fetch=1)
    return product

def create_product(data):    

    product_name = data.model_dump()['product_name']
    product_description = data.model_dump()['product_description']
    fk_product_type_id = data.model_dump()['fk_product_type_id']
    
    query = 'INSERT INTO product (product_name, product_description, fk_product_type_id) VALUES (%s, %s, %s)'
    values =  (product_name, product_description,fk_product_type_id)
    execute_query(query,values)
    return jsonify({'message': 'Product created successfully!'}), 201


def update_product(id,data):  

    product_name = data.model_dump()['product_name']
    product_description = data.model_dump()['product_description']
    fk_product_type_id = data.model_dump()['fk_product_type_id']

    query='UPDATE product SET product_name = %s, product_description = %s,  fk_product_type_id = %s WHERE id = %s'
    values=(product_name, product_description,fk_product_type_id,id)
    execute_query(query,values)
    return jsonify({'message': 'Product updated successfully!'}), 200


def delete_product(id):
    query = 'DELETE FROM product WHERE id = %s'
    values = id
    execute_query(query,values)
    return jsonify({'message': 'Product deleted'}), 201

def execute_query(query,values=None,fetch=0):
    try:
        result=None
        conn = get_db_connection()
        if fetch==0:
            cursor = conn.cursor()
            cursor.execute(query,values)
            conn.commit()
        if fetch==1:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query,values)
            result = cursor.fetchone()
        if fetch==2:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print("Column Names:", column_names)
            result = []
            for row in rows:
                # Create a dictionary for each row
                row_dict = dict(zip(column_names, row))
                result.append(row_dict)

        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return jsonify({'error': str(e)}), 500


