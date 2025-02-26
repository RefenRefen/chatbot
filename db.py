from pymongo import MongoClient
from datetime import datetime

def push_user_message(username: str, message: str):
    """Pushes a user message into MongoDB."""

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URI if needed
    db = client["chat_app"]  # Database name
    collection = db["messages"]  # Collection name

    # Create a document
    msg_doc = {
        "username": username,
        "message": message,
        "timestamp": datetime.utcnow()  # Store time in UTC format
    }

    # Insert into MongoDB
    result = collection.insert_one(msg_doc)

    # Return the inserted ID
    return result.inserted_id


def get_user_last_messages(username: str, limit=3):
    """Retrieves the last `limit` messages from a specific user in MongoDB."""

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Update with your MongoDB URI if needed
    db = client["chat_app"]  # Database name
    collection = db["messages"]  # Collection name

    # Fetch the last `limit` messages from the given user, sorted by timestamp (newest first)
    messages = collection.find({"username": username}).sort("timestamp", -1).limit(limit)

    # Convert messages to a list and return
    message_string = " | ".join([msg["message"] for msg in messages])

    return message_string