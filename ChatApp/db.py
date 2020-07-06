from pymongo import MongoClient
from werkzeug.security import generate_password_hash

from user import User

client = MongoClient("mongodb+srv://admim:admin@chatapp.m4qmx.mongodb.net/<dbname>?retryWrites=true&w=majority")

chat_db = client.get_database("ChatDB")
users_collections = chat_db.get_collection("users")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collections.insert_one({'_id': username, 'email': email, 'password': password_hash})

def get_user(username):
    user_data = users_collections.find_one({'_id': username})
    return User(user_data['_id'], user_data['email'], user_data['password']) if user_data else None



