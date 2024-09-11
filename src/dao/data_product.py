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

def list_products():
    # Connect to the MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]
    print("Column Names:", column_names)

    res = []
    
    for row in rows:
        # Create a dictionary for each row
        row_dict = dict(zip(column_names, row))
        res.append(row_dict)
    
    # Close the connection
    cursor.close()
    conn.close()
    
    # Convert to JSON and return
    return res

def get_product(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM product WHERE id = %s', (id,))
        product = cursor.fetchone()
        cursor.close()
        conn.close()
        if product:
            return jsonify(product), 200
        else:
            return jsonify({'message': 'Product not found'}), 404
    except Error as e:
        return jsonify({'error': str(e)}), 500


def create_product(data):
    name = data['name']
    description = data['description']
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO product (name, description) VALUES (%s, %s)', (name, description))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Product created successfully!'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

def update_product(id,data):
    name = data['name']
    description = data['description']
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE product SET name = %s, description = %s WHERE id = %s', (name, description, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Product updated successfully!'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

def delete_product(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM product WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        if cursor.rowcount > 0:
            return jsonify({'message': 'Product deleted successfully!'}), 200
        else:
            return jsonify({'message': 'Product not found'}), 404
    except Error as e:
        return jsonify({'error': str(e)}), 500
    