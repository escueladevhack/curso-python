from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database

posts = db.posts

import datetime

p1 = dict()
p1["title"] = "Hello world"
p1["body"] = "lorem ipsum"
p1["pub_date"] = datetime.datetime.utcnow()
inserted_post = posts.insert_one(p1)

list(posts.find())