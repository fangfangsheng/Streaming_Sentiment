import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost/')
# Naming the database
db = client['twitter_collect_db']
# Getting a collection, like table in sql
collection = db['twitter-api']

print(collection.find_one())
print('finish')

# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.utcnow()}

## Inserting a Document
# collection_id =collection.insert_one(post).inserted_id

## Inserting many Documents, passing a list as the first argument to insert_many().
# new_posts = [{"author": "Mike",
#              "text": "Another post!",
#              "tags": ["bulk", "insert"],
#              "date": datetime.datetime(2009, 11, 12, 11, 14)},
#              {"author": "Eliot",
#               "title": "MongoDB is fun",
#               "text": "and pretty easy too!",
#               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
#
# result = collection.insert_many(new_posts)

## Listing all of the collections in our database
# print(db.list_collection_names())

## Query one document with find_one()
#print(collection.find_one())


## Query all documents with find()
# for post in collection.find():
#     print(post)
# Count documents match a query
# print(collection.count_documents({"author": "Mike"}))


# db.contacts.insert({
#  "id":db.contacts.find().Count()+1,
#  "name":"John Doe",
#  "emails":[
#     "john@doe.com",
#     "john.doe@business.com"
#  ],
#  "phone":"555111322",
#  "status":"Active"
# });
#
# for post in collection.find():
#     print(post)