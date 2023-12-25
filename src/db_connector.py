# db_connector.py

import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin9182",
        database="bank_manage"
    )
