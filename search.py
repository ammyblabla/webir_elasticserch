import requests
import json

localhost = 'http://localhost:9200/'
search_url = '_search?q='
query = 'note 9'

url = localhost + search_url + query
r = requests.get(url)
res_raw = json.loads(r.text)
search_result = []

for one_res in res_raw['hits']['hits']:
   one_res_source = one_res['_source']
   one_res_source['_score'] = one_res['_score']
   search_result.append(one_res_source) 