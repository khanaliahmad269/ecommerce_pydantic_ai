"""
Database configuration and MongoDB connection setup

"""

from pymongo import MongoClient

from dotenv import load_dotenv
import os

#loading environment variables from the .env file at root

load_dotenv(dotenv_path=os.path.join(os.getcwd(),".env"))

#connect mongo db

MONGO_URI=os.getenv("MONGO_URI")

#initializing the mongo client

client=MongoClient(MONGO_URI)
db=client["ecommerce_db"]

#Collections

users_collection =db["users"]
products_collection =db["products"]
orders_collection =db["orders"]
cart_collection=db["cart"]
