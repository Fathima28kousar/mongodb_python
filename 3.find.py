import pymongo
if __name__=="__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['fathima']
    collection = db['mySampleCollectionForFathima']
    # one = collection.find_one({'name':'fathima'})
    # print(one)

    # count = collection.count_documents({'Name': 'Fathima'}).limit(1)
    # print(count)
    #print(f"Number of documents with Name 'Fathima': {count}")

    # all = collection.find({'Name':'Fathima'}).limit(1)
    #print(all.count())
