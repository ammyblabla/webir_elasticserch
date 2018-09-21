curl -XPUT 'localhost:9200/ku?pretty' -H 'Content-Type: application/json' -d
'
{
    "mappings": {
        "webpage": {
            "properties": {
                "BaseUrl": { "type": "keyword"},
                "Url": {"type": "keyword"},
                "Title": {"type": "text", "analyzer": Thai},
                "Body": {"type": "text", "analyzer": Thai}
                "Encoding": {"type": "keyword"},
                "Links": {"type": "keyword"},
                "Crawling_date": {
                    "type": "date",
                    "format": "yyyy-MM-dd HH:mm:ss"
                },

            }      
        }
    }
}'