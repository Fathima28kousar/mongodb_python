import pymongo
if __name__=="__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['fathima']
    collection = db['mySampleCollectionForFathima']

    #delete One
    # rec = {'Name':'Fathima'}
    # collection.delete_one(rec)

    #delete Many
    rec = {'name':'fathima'}
    up = collection.delete_many(rec)
    print(up.deleted_count)