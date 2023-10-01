import pymongo
if __name__=="__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['fathima']
    collection = db['mySampleCollectionForFathima']
    #insert one
    # dictionary = {'name':'fathima','marks':50}
    # collection.insert_one(dictionary)

    # dictionary = {'name':'kousar','marks':49}
    # collection.insert_one(dictionary)

    #insert Many
    list = [
        {'_id':1,'Name':'Fathima','Location':'London','Marks':90},
        {'_id':2,'Name':'Kousar','Location':'US','Marks':98},
        {'_id':3,'Name':'Naseera','Location':'UK','Marks':70},
        {'_id':4,'Name':'Lubna','Location':'Dubai','Marks':100},
    ]
    collection.insert_many(list)