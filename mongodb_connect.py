from pymongo import MongoClient
import pprint


def get_docs_db(db, collection):
   client = MongoClient()
   db = client['mobile_search']
   collection = db['docs']
   all_docs = []
   nbD = 0
   for docs in collection.find():
      all_docs.append(docs)
      nbD += 1
      if nbD % 1000 == 0:
         print(nbD)
   client.close()
   return all_docs
   
