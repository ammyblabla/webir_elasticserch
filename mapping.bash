curl -XPUT 'localhost:9200/ku?pretty' -H 'Content-Type: application/json' -d'
{
	"settings" : {
		"number_of_shards": 3,
		"number_of_replicas": 0
	},
  "mappings" : {
		"webpage": {
			"properties": {
				"BaseUrl": {"type" : "keyword"},
				"Url": {"type" : "keyword"},
				"Title": {"type" : "text", "analyzer": "thai"},
				"Body": {"type" : "text", "analyzer": "thai"},
				"Encoding": {"type" : "keyword"},
				"Links": {"type" : "keyword"},
				"Crawling_date": {
					"type": "date",
					"format": "yyyy-MM-dd HH:mm:ss"
				}
			}
		}
 	}
}'
