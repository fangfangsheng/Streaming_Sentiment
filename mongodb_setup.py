import pymongo
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost/')
# Naming the database
db = client['twitter_collect_db']
# Getting a collection, like table in sql
collection = db['twitter-api-health']

print(collection.find_one())
print('finish')

