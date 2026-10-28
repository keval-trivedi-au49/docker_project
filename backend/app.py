from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

frontend_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "frontend")

app = Flask(__name__)
mongo_uri = os.getenv("MONGO_URI")
CORS(app)

client = MongoClient(mongo_uri)
db = client["fullstack_app"]
users = db["drivers"]


@app.route("/api/submit", methods=["POST"])
def submit():

    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        if not name:
            return jsonify({"message": "Name is required"}),400
        if not email:
             return jsonify({"message": "Email is required"}),400
        user_data = {
            "name": name,
            "email": email
        }

        users.insert_one(user_data)
        return jsonify({"message": "User created successfully"}),200

    except Exception as error:
        return jsonify({"message": str(error)}),500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)