import json
import sys
import time
from elasticsearch import Elasticsearch
import pathlib
import codecs
from pymongo import MongoClient

class my_elasticSearch():
   ES_HOST = 'http://localhost:9200/'
   INDEX = 'mobile'; DOCTYPE = 'webpage'
   es = Elasticsearch()
   def __init__(self, option):
      self.setting(option)

   def get_dataset_filename(self):
      currentDirectory = pathlib.Path('dataset')
      currentPattern = "*.json"
      currentFiles = []
      for currentFile in currentDirectory.glob(currentPattern):  
         currentFiles.append(str(currentFile))
      return currentFiles

   def get_json_db(self,database, collection):
      client = MongoClient()
      # db = client['mobile_search']
      # collection = db['docs']
      db = client[database]
      collection = db[collection]
      all_docs = []
      nbD = 0
      for docs in collection.find():
         all_docs.append(docs)
         del docs['_id']
         nbD += 1
         if nbD % 1000 == 0:
            print(nbD)
      client.close()
      return all_docs


   def get_json_file(self):
      filenames = self.get_dataset_filename()
      all_list = []
      for filename in filenames:
         print(filename)
         try:
            with codecs.open(filename, 'r',encoding='utf-8') as f:
               lines = f.readlines()
            # for line in lines:
            # keys = None
            for i in range(len(lines)):
               line = lines[i]
               line = line.strip()
               obj = json.loads(line)
               if list(obj.keys()) != ['link', 'title', 'domain_name', 'base_url', 'text', 'remove_stopword_word_tokens', 'remove_stopword_text']:
                  print(i)
               all_list.append(obj)
         except Exception as e:
            print(i)
            print(e)

      return all_list

   def indexDoc(self,doc):
      myid = doc['link']
      res = self.es.index(index=self.INDEX, doc_type = self.DOCTYPE, id=myid, body=doc)
      return True

   def setting(self,option):
      if option == "file":
         JSONdocs = self.get_json_file()
      elif option == "db":
         JSONdocs = self.get_json_db('mobile_search','docs')
      print('finish read file')
      # print(len(all_list))

      start_time = time.time()
      nbD = 0
      print('indexing.....')
      for i in JSONdocs:
      #     i['remove_stopword_word_tokens'] = ''
         del i['remove_stopword_word_tokens']
         self.indexDoc(i)
         nbD += 1
         if nbD % 1000 == 0:
            print(nbD)
      print('\n', nbD, 'document(s) indexed.')
      end_time = time.time()
      print('Running time: ', str(end_time-start_time), 'seconds.')

   # print(get_dataset_filename())