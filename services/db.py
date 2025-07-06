# services/db.py
from pymongo import MongoClient
import os

#This line tries to get a value from your computer's environment variables.
# "MONGO_URI" is the name of the environment variable it's looking for.
# "mongodb://localhost:27017" is the default value it will use if it doesn't find that environment variable.
MONGO_URI = "mongodb+srv://mailkshitiz17:Anshdeep1704@kshitizcluster17.ipvcixe.mongodb.net/?retryWrites=true&w=majority&appName=KshitizCluster17"  # or use Atlas URI

# This creates a connection to MongoDB using the URI provided.
# client is now a handle to interact with the MongoDB server.
client = MongoClient(MONGO_URI)

# This accesses a database named faq_chatbot.
# If it doesn't exist, MongoDB will create it when you insert the first document.
db = client["faq_chatbot"]  # database name

# upload_collection And queries_collection are just variable names to represent collections in database(faq_chatbot) these collections are uploads & queries
uploads_collection = db["uploads"]
queries_collection = db["queries"]

# faq_chatbot (cabinet)
# ├── uploads (drawer)   --> holds info about uploaded PDFs
# └── queries (drawer)   --> holds info about questions users ask
