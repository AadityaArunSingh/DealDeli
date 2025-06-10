import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql_container"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", os.getenv("MYSQL_ROOT_PASSWORD", "UoS@2025")),
        database=os.getenv("MYSQL_DATABASE", "dealdeli_data")
    )
