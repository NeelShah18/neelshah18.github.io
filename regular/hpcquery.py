import json
import elasticsearch

def main():
    es = elasticsearch.Elasticsearch()
    try:
        #Body cotains your query of elasticsearch
        #Tutorial for query bulding: https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl.html
        output = es.search(index="*", body={"query":{
            "match":
                {"text":
                    "women woman health issues issue disease diseases common top reproductiveheal reprodutive health"
                    }
                }
            })
        #change the name of your output file below. it always be in JSON format
        with open("/home/nshah5/<Name of your file>.json","w") as f:
            json.dump(output, f, sort_keys=True, indent=4)
    except Exception as e:
        print("Error "+str(e))
    return None

if __name__=="__main__":
    main()
    #print("Check your file at /home/nshah5/<name of your file>.json")
