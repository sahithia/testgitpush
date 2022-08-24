import pymongo

client = pymongo.MongoClient("mongodb+srv://Chikki:Kids2018@rainbow.kkpwfof.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name": "sahithi",
    "email": "sahithi@gmail.com",
    "surname": "A"
}

db1=client['mongotest']
coll = db1['test']
coll.insert_one(d)