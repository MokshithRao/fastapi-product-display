import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "test",
        password = "123456",
        database = "product_db"
    )

    return connection

