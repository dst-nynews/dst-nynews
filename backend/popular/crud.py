from bson.objectid import ObjectId

from database import mongodb

# # Verify if MongoDB client is instanciated and/or accessible
# # (might not be pythonic)
# try:
#     mongodb
# except NameError:
#     from motor.motor_asyncio import AsyncIOMotorClient
#     from config import settings

#     mongodb_client = AsyncIOMotorClient(settings.MONGO_DETAILS)
#     mongodb = mongodb_client.testasync


# popular_collection = mongodb.get_collection("popular_collection")
popular_collection = mongodb.get_collection("Populars")


# HELPER functions #
# for parsing the results from a database query into a Python dict.
def popular_helper(popular) -> dict:
    return {
        "id": str(popular["_id"]),
        "most_popular_type": popular["most_popular_type"],
        "search_period": popular["search_period"],
        "search_month": popular["search_month"],
        "search_day": popular["search_day"],
        "created_at": popular["created_at"],
        "Articles": popular["Articles"],
    }


# CRUD operations #

# Retrieve all group of popular articles present in the database
async def read_popular_index():
    populars = []
    async for popular in popular_collection.find():
        populars.append(popular_helper(popular))
    return populars


# Retrieve a group of popular articles with a matching ID
async def read_popular(id: str) -> dict:
    popular = await popular_collection.find_one({"_id": ObjectId(id)})
    if popular:
        return popular_helper(popular)


# Add a new group of popular articles  into to the database
async def create_popular(popular_data: dict) -> dict:
    popular = await popular_collection.insert_one(popular_data)
    created_popular = await popular_collection.find_one({"_id": popular.inserted_id})
    return popular_helper(created_popular)


# Update a group of popular articles with a matching ID
async def update_popular(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    popular = await popular_collection.find_one({"_id": ObjectId(id)})
    if popular:
        updated_popular = await popular_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_popular:
            return True
        return False


# Delete a group of popular articles from the database
async def delete_popular(id: str):
    popular = await popular_collection.find_one({"_id": ObjectId(id)})
    if popular:
        await popular_collection.delete_one({"_id": ObjectId(id)})
        return True
