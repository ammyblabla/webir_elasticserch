import pprint
from search import searcher
obj = searcher()
query = 'note9'
result = obj.search(query, sum_op = 'text', SENTENCES_COUNT=2)
# print(pprint.pprint(result))
