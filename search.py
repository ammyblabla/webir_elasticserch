import requests
import json
from summarizer import summarizer

class searcher():
   localhost = 'http://localhost:9200/'
   search_url = '_search?q='

   def __init__(self):
      pass

   def search(self,query):
      url = self.localhost + self.search_url + query
      r = requests.get(url)
      res_raw = json.loads(r.text)
      search_result = []

      for one_res in res_raw['hits']['hits']:
         one_res_source = one_res['_source']
         one_res_source['_score'] = one_res['_score']
         one_res_source['summarize'] = summarizer(one_res_source['link'])
         del one_res_source['remove_stopword_text']
         search_result.append(one_res_source) 
      return search_result