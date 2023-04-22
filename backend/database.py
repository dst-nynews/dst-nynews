import os

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

# MongoDB setup #
# Async DB connection with Motor client
mongo_host = os.getenv("MONGO_CLIENT_HOST")  # Cloud Atlas connection
# mongo_host = os.getenv("MONGO_LOCAL_HOST")  # Local MongoDB connection
mongodb_client = AsyncIOMotorClient(mongo_host)

mongodb = mongodb_client["NYTimes"]
# db_name = os.getenv("MONGO_DB_NAME")
# mongodb = mongodb_client[db_name]
