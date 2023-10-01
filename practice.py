import pymongo
if __name__=="__main__":
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["fathima"]
    collection = db["mySampleCollectionForFathima"]

    # dictionary = {"name":"Priyanka","city":"china"}
    # collection.insert_one(dictionary)
    # dictionary = {"name":"lubna","marks":94,"city":"bombay"}
    # collection.insert_one(dictionary)

    # insertThese =[{"name":"Rahul","marks":100,"city":"bangalore"},
    #               {"name":"Sonia","marks":200,"city":"delhi"},
    #               {"name":"Priyanka","marks":300,"city":"mumbai"},
    #               {"name":"Modi","marks":400,"city":"chatthisgarh"}]
    
    # collection.insert_many(insertThese)

    # one = collection.find_one({"name":"Rahul"})
    # print(one)

    '''    all = collection.find({"name":"Priyanka"},{"name":0,"_id":0})
    for item in all:
        print(item)'''

    # count = collection.count_documents({"name":"Priyanka"})
    # print(count)

    # alldatabases = client.list_database_names()
    # print(alldatabases)

    # col = client["fathima"]
    # print(col.list_collection_names())

    # prev = {"name":"Priyanka"}
    # nextt = {"$set":{"city":"mumbai"}}
    # collection.update_one(prev,nextt)

    # prev = {"name":"Priyanka"}
    # nextt = {"$set":{"city":"mumbai"}}
    # up = collection.update_many(prev,nextt)
    # print(up.modified_count)

    # rec = {"name":"Priyanka"}
    # up = collection.delete_many(rec)
    # print(up.deleted_count)

    # all = collection.find({"name":"Priyanka"},{"name":0})
    # for item in all:
    #     print(item)

    
    # all = collection.find({"Name":"Naseera"})
    # print(collection.count_documents({}))
    # for item in all:
    #     print(item)