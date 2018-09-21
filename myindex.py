# -*- coding: utf-8 -*-
import json
import gzip
import os, sys
import time
from elasticsearch import Elasticsearch
def parseHTML(fn):
    res = []; nbDoc = 0
    f = gzip.open(fn)
    for i in f:
        jj = json.loads(i)
        nbDoc += 1
        res.append(jj)
        if nbDoc%100==0:
            print('.', end='')
            sys.stdout.flush()
    print(nbDoc, 'documents found.')
    return res

def indexDoc(doc):
    myid = doc['Url']
    res = es.index(index=INDEX, doc_type = DOCTYPE, id=myid, body=doc)
    return True

def parseHTML2(fn):
    res = []; nbDoc = 0
    for root, dirs, files in os.walk(fn):
        for name in files:
            nbDoc += 1
            fname = os.path.join(root,name)
            f = open(fname, encoding='utf-8')
            page = f.read()
            if nbDoc%100==0:
                print('.', end='')
                sys.stdout.flush()
            # DIY
            # แกะ title, body
            res.append(page)
    print(nbDoc, 'documents found.')
    return res

# main begins here
start_time = time.time()
fn = 'webpage.txt.gz'
JSONdocs = parseHTML(fn)
ES_HOST = 'http://localhost:9200/'
INDEX = 'ku'; DOCTYPE = 'webpage'
es = Elasticsearch(ES_HOST)
# es.index(index=INDEX, doc_type=DOCTYPE, id=JSONdocs[0]['Url'], body=JSONdocs[0])
# indexDoc(JSONdocs[0])
# indexDoc(JSONdocs[1])
nbD = 0
for i in JSONdocs:
    i['Links'] = ''
    indexDoc(i)
    nbD += 1
    if nbD%100==0:
        print(',', end='')
print('\n', nbD, 'document(s) indexed.')
end_time = time.time()
print('Running time: ', str(end_time-start_time), 'seconds.')

# วิธีการ search ให้พิมพ์ลง url ของ browser หรือใช้คำสั่ง curl
# http://localhost:9200/_search?q=computer
# http://localhost:9200/_search?q=Title=%E0%B8%A0%E0%B8%B2%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%8A%E0%B8%B2%E0%B8%A7%E0%B8%B4%E0%B8%A8%E0%B8%A7%E0%B8%81%E0%B8%A3%E0%B8%A3%E0%B8%A1%E0%B8%84%E0%B8%AD%E0%B8%A1%E0%B8%9E%E0%B8%B4%E0%B8%A7%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C