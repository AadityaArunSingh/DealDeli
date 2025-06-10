import mysql.connector
import os

def get_connection():
    """Create and return a MySQL connection using environment variables."""

    host = os.environ.get("MYSQL_HOST", "mysql_container")
    user = os.environ.get("MYSQL_USER", "root")
    password = os.environ.get("MYSQL_PASSWORD", "password")
    database = os.environ.get("MYSQL_DATABASE", "DealDeli_data")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
