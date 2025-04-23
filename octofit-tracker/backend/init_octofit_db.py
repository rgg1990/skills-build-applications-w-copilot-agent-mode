from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Create or switch to the octofit_db database
db = client["octofit_db"]

# Create collections
collections = ["users", "teams", "activity", "leaderboard", "workouts"]
for collection in collections:
    db.create_collection(collection)

# Ensure unique index on the email field in the users collection
db["users"].create_index("email", unique=True)

# List all collections in the database
print("Collections in octofit_db:", db.list_collection_names())
