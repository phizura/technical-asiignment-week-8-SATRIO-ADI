
import pymongo 
import datetime


client = pymongo.MongoClient("mongodb+srv://retipe23:yesser@cluster0.vmzrg.mongodb.net/?retryWrites=true&w=majority")
db = client.MyDatabase
collection = db.monggo

def save_to_base(kecepatan,latitude,longitude):
    try:
        data = {
            "kecepatan": kecepatan,
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now()
        }

        rec_id1 = collection.insert_one(data)

        print("Data inserted with record", rec_id1)
        return True,None
    except Exception as e:
        return False,str(e)
