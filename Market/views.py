from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from elasticsearch import Elasticsearch
# Create your views here.
@csrf_protect
def home(request):
    es = Elasticsearch('http://119.3.142.210:9200')
    query_computer = {
        'query': {
            'query_string': {
                'default_field': 'description',
                'query': "电脑"
            }
        },
        'highlight': {
            'fields': {
                'description': {}
            }
        }
        ,'size':15
    }
    res = es.search(index='jdonggoods', body=query_computer)
    result = {}
    result_computer = []
    for source in res['hits']['hits']:
        result_computer.append(source['_source'])
    result['computer'] = result_computer
    result['total'] = res['hits']['total']['value']
    print(result)
    return render(request,"index.html",context=result)
@csrf_protect
def search(request):
    query = request.POST.get('query')
    print(query)
    es = Elasticsearch('http://119.3.142.210:9200')
    query_computer = {
    "size": 15,
    "query": {
    "multi_match": {
      "query": query,
      "fields": ["title","description"]
    }
  }
}
    res = es.search(index='jdonggoods', body=query_computer)
    result = {}
    result_computer = []
    for source in res['hits']['hits']:
        result_computer.append(source['_source'])
    result['computer'] = result_computer
    result['total'] = res['hits']['total']['value']
    print(result)
    return render(request, "index.html", context=result)