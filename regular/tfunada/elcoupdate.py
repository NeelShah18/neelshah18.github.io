#import elasticsearch
import json

temp_data = {}
with open("/mnt/d/github/neelshah18.github.io/regular/ansUpdate.json","r") as f:
    temp_data = json.load(f)
def main():
    i=0
    #es = elasticsearch.Elasticsearch()
    mappings = {
    'post': {
        'properties': {
            'country': {'type': 'text'},
            'freq': {'type': 'long'},
            'location': {'type': 'geo_point'}
            }
        }
    }
    #body = {'mappings': mappings}
    #es.indices.create(index="heat1", body=body)
    for data in temp_data:
        temp_dic = {}
        temp_dic = data
        print(temp_dic)
        i = i+1
        #es.index(index='heat1', doc_type='post', id=i, body=temp_dic)
        print(i)
    return None
if __name__=="__main__":
    main()
