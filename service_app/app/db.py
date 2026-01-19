from pymongo import MongoClient

client = MongoClient("mongodb+srv://rushidhar:rushidharr@projects.sko4wr9.mongodb.net/?retryWrites=true&w=majority")
db = client.microservice_db
collection = db.items
