from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB URL from .env
MONGO_URL = os.getenv("MONGO_URL")

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)

    # Test connection
    client.server_info()

    print("✅ MongoDB connected successfully")

except Exception as e:
    print("❌ MongoDB connection failed:", e)

# Database
db = client["fitbuddy"]

# Collections
users_collection = db["users"]
plans_collection = db["workout_plans"]


# SAVE USER
def save_user(name, age, weight, goal, intensity):

    try:

        user = {
            "name": name,
            "age": age,
            "weight": weight,
            "goal": goal,
            "intensity": intensity
        }

        result = users_collection.insert_one(user)

        return str(result.inserted_id)

    except Exception as e:
        print("save_user error:", e)
        return None


# SAVE WORKOUT PLAN
def save_plan(user_id, plan):

    try:

        workout = {
            "user_id": user_id,
            "original_plan": plan,
            "updated_plan": None
        }

        plans_collection.insert_one(workout)

    except Exception as e:
        print("save_plan error:", e)


# UPDATE PLAN
def update_plan(user_id, updated_text):

    try:

        plans_collection.update_one(
            {"user_id": user_id},
            {"$set": {"updated_plan": updated_text}}
        )

    except Exception as e:
        print("update_plan error:", e)


# GET ORIGINAL PLAN
def get_original_plan(user_id):

    try:

        plan = plans_collection.find_one({"user_id": user_id})

        if plan:
            return plan.get("original_plan")

        return None

    except Exception as e:
        print("get_original_plan error:", e)
        return None


# GET USER
def get_user(user_id):

    try:

        user = users_collection.find_one({"_id": ObjectId(user_id)})

        if user:
            user["_id"] = str(user["_id"])

        return user

    except Exception as e:
        print("get_user error:", e)
        return None


# GET ALL USERS (Admin Dashboard)
def get_all_users():

    try:

        users = list(users_collection.find())

        for user in users:
            user["_id"] = str(user["_id"])

        return users

    except Exception as e:
        print("get_all_users error:", e)
        return []