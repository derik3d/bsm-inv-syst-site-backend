from flask import jsonify
import mysql.connector

# MySQL connection setup
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "bigstoremanager",
}


def get_db_connection():
    connection = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"],
    )
    return connection


def list_general(table):
    query = "SELECT * FROM " + table
    products = execute_query(query, fetch=2)
    return products


def get_general(table, id):
    query = "SELECT * FROM " + table + " WHERE id = %s"
    values = (id,)
    product = execute_query(query, values, fetch=1)
    return product


def create_general(table, data):

    model_dump = data.model_dump()
    keys = model_dump.keys()
    field_to_ignore = "id"

    # organize values tuple

    values_tuple = tuple(
        value for key, value in model_dump.items() if key != field_to_ignore
    )

    # build query

    sss = []
    query_mid = []

    for item in keys:
        if item != "id":
            query_mid.append(item)
            sss.append("%s")

    query_start = "INSERT INTO " + table + " ("
    query_string_mid = ", ".join(query_mid)
    id_query_part = ") VALUES ( " + ", ".join(sss) + " )"

    forming_query = []
    forming_query.append(query_start)
    forming_query.append(query_string_mid)
    forming_query.append(id_query_part)
    query = " ".join(forming_query)

    # print query

    print(query)
    print(values_tuple)

    execute_query(query, values_tuple)
    return jsonify({"message": "item from " + table + " created successfully!"}), 201


def update_general(table, id, data):

    print(data.model_dump())

    model_dump = data.model_dump()
    keys = model_dump.keys()
    field_to_ignore = "id"

    # organzie values tuple

    values_tuple = tuple(
        value for key, value in model_dump.items() if key != field_to_ignore
    )

    values_tuple += (model_dump[field_to_ignore],)

    # create query

    query_mid = []
    for item in keys:
        if item != "id":
            query_mid.append(item + " = %s")

    query_start = "UPDATE " + table + " SET"
    query_string_mid = ", ".join(query_mid)
    id_query_part = "WHERE id = %s"

    forming_query = []
    forming_query.append(query_start)
    forming_query.append(query_string_mid)
    forming_query.append(id_query_part)

    query = " ".join(forming_query)

    print(query)
    print(values_tuple)

    execute_query(query, values_tuple)
    return jsonify({"message": "item from " + table + " updated successfully!"}), 200


def delete_general(table, id):
    query = "DELETE FROM " + table + " WHERE id = %s"
    values = (id,)
    execute_query(query, values)
    return jsonify({"message": "item from " + table + " deleted"}), 201


def execute_query(query, values=None, fetch=0):
    try:
        result = None
        conn = get_db_connection()
        if fetch == 0:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()
        if fetch == 1:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, values)
            result = cursor.fetchone()
        if fetch == 2:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()

        cursor.close()
        conn.close()
        return result
    except Exception as e:
        return jsonify({"error": str(e)}), 500
