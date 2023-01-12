from elasticsearch import Elasticsearch
from json import loads

es = Elasticsearch('http://192.168.10.132:9200')
query = {
    'query': {
        'query_string': {
            'default_field': 'description',
            'query': "手机"
        }
    },
    'size': 4,
}
res = es.search(index='goods', body=query)
result = loads(res.body)
print(result)
