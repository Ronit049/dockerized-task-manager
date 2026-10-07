import os

from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "task_manager")

client = MongoClient(MONGO_URL)

db = client[DATABASE_NAME]

tasks_collection = db["tasks"]
