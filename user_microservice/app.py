from flask import Flask
from flask_cors import CORS
from routes import routes
from db import init_db

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (for frontend to call backend)
CORS(app)

###limit to specific domains
#CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

###
#@app.route('/')
#def index():
 #   return "Welcome to the API!"
###
# Register routes from the Blueprint
app.register_blueprint(routes)

# Run the Flask application
if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001,debug=True)

    #app.run(debug=True)  # You can set debug=False in production
