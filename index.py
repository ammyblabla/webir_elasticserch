import json
import sys
import time
from elasticsearch import Elasticsearch
import pathlib
import codecs


def get_dataset_filename():
   currentDirectory = pathlib.Path('dataset')
   currentPattern = "*.json"
   currentFiles = []
   for currentFile in currentDirectory.glob(currentPattern):  
      currentFiles.append(str(currentFile))
   return currentFiles

def get_json():
   filenames = get_dataset_filename()
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

def indexDoc(doc):
   myid = doc['link']
   res = es.index(index=INDEX, doc_type = DOCTYPE, id=myid, body=doc)
   return True

JSONdocs = get_json()
print('finish read file')
# print(len(all_list))

ES_HOST = 'http://localhost:9200/'
INDEX = 'mobile'; DOCTYPE = 'webpage'
es = Elasticsearch()

start_time = time.time()
nbD = 0
for i in JSONdocs:
#     i['remove_stopword_word_tokens'] = ''
   del i['remove_stopword_word_tokens']
   indexDoc(i)
   nbD += 1
   if nbD%100==0:
      print(',', end='')
print('\n', nbD, 'document(s) indexed.')
end_time = time.time()
print('Running time: ', str(end_time-start_time), 'seconds.')

# print(get_dataset_filename())