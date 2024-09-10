from flask import  jsonify
import mysql.connector

# MySQL connection setup
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'sfs2x'
}

def get_db_connection():
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )
    return connection

def index():
    # Connect to the MySQL database
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user LIMIT 5")
    rows = cursor.fetchall()

    column_names = [i[0] for i in cursor.description]
    print("Column Names:", column_names)
    # Column Names: ['username', 'pass']


    res = {
        "data" : []
    }
    
    for row in rows:
        res["data"].append(row)  # Close the connection
    cursor.close()
    conn.close()
    
    return res