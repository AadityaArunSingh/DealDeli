# first source venv/bin/activate
# flask --app app run

from flask import Flask, jsonify, request,render_template
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.exc import OperationalError
from urllib.parse import quote_plus
from sqlalchemy import text

app = Flask(__name__)
CORS(app, origins=["http://localhost:5501"])


# Load from env or fallback
user = os.getenv("MYSQL_USER", "root")
password = quote_plus(os.getenv("MYSQL_PASSWORD", "UoS@2025"))  # Escape special chars
host = os.getenv("MYSQL_HOST", "mysql_container")
db_name = os.getenv("MYSQL_DATABASE", "dealdeli_data")

# Use safely encoded password
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def db_check():
    try:
        result = db.session.execute(text("SELECT COUNT(*) FROM products"))
        count = result.fetchone()[0]
        return jsonify({"status": "connected", "total_products": count})
    except OperationalError as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/compare")
def compare_product():

    query_name = request.args.get("name")
    if not query_name:
        return jsonify({"error": "Please provide a product name using ?name="}), 400
    
    sql = text("""
        SELECT 
            `Product Name` AS name, 
            CAST(`Price in GBP` AS DECIMAL(10,2)) AS price, 
            `Category` AS category, 
            `Image URL` AS image, 
            `Product URL` AS link
        FROM products
        WHERE LOWER(`Product Name`) LIKE :pattern
        ORDER BY price ASC
    """)
    pattern = f"%{query_name.lower()}%"

    try:
        result = db.session.execute(sql, {"pattern": pattern})
        products = [dict(row._mapping) for row in result]
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(products)

if __name__ == "__main__":
    app.run()

# compare?name=apple


