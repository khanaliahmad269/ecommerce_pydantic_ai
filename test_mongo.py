from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"), serverSelectionTimeoutMS=5000)

try:
    print("Trying to connect...")
    print(client.server_info())
    print("Connected!")
except Exception as e:
    print(type(e).__name__)
    print(e)