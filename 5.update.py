import pymongo
if __name__=="__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['fathima']
    collection = db['mySampleCollectionForFathima']

    prev = {'Name':'Fathima'}
    nextt = {'$set':{'Location':'Mumbai'}}

    #update One
    # collection.update_one(prev,nextt)

    #update Many
    up = collection.update_many(prev,nextt)
    print(up.modified_count)