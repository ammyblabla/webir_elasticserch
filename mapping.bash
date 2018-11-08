curl -XPUT 'localhost:9200/mobile?pretty' -H 'Content-Type: application/json' -d '
{
   "settings" : {
      "number_of_shards": 3,
      "number_of_replicas": 0
   },
  "mappings" : {
      "webpage": {
         "properties": {
            "link": {"type" : "keyword"},
            "title": {"type" : "text"}, 
            "domain_name": {"type" : "keyword"}, 
            "base_url": {"type" : "keyword"}, 
            "text": {"type" : "text"},
            "remove_stopword_text":  {"type" : "text"}
         }
      }
   }
}'