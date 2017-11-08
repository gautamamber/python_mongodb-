from pymongo import MongoClient
MONGODB_URI = "mongodb://amber:amber@ds155325.mlab.com:55325/amberamity"
client = MongoClient(MONGODB_URI, connectTimeoutMS=30000)
db = client.get_database("amberamity")
user_records = db.user_records

def getRECORD(user_id):
    records = user_records.find_one({"user_id":user_id})
    return records

def pushRECORD(record):
    user_records.insert_one(record)

def updateRecord(record, updates):
    user_records.update_one({'_id': record['_id']},{
                              '$set': updates
                              }, upsert=False)
record = {
    
    "name": "gautam",
    "age": "20",
    "class" : "twelth"
}
pushRECORD(record)



