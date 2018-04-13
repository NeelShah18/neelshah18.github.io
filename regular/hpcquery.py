import json
import elasticsearch
import math

def scroll(index, doc_type, query_body, page_size=100, debug=False, scroll='2m'):
    es = elasticsearch.Elasticsearch()
    page = es.search(index=index, doc_type=doc_type, scroll=scroll, size=page_size, body=query_body)
    sid = page['_scroll_id']
    scroll_size = page['hits']['total']
    total_pages = math.ceil(scroll_size/page_size)
    page_counter = 0
    if debug:
        print('Total items : {}'.format(scroll_size))
        print('Total pages : {}'.format( math.ceil(scroll_size/page_size) ) )
    # Start scrolling
    while (scroll_size > 0):
        # Get the number of results that we returned in the last scroll
        scroll_size = len(page['hits']['hits'])
        print(scroll_size)
        if scroll_size>0:
            if debug:
                print('> Scrolling page {} : {} items'.format(page_counter, scroll_size))
            yield total_pages, page_counter, scroll_size, page
        # get next page
        page = es.scroll(scroll_id = sid, scroll = '2m')
        page_counter += 1
        # Update the scroll ID
        sid = page['_scroll_id']

def main():
    es = elasticsearch.Elasticsearch()
    # <-------------------------------------------------->
    #here you can use your query: edit it as you want
    #Tutorial for query building: https://www.elastic.co/guide/en/elasticsearch/reference/6.2/query-dsl.html
    #And you can write on youyr query just make sure about foramte
    
    query = {
            "match":
                {"text":
                    "your keywords for searching example: pizza, burger"
                    }
            }
    #Name of your output file: Please change
    #pattern : yourname_Query_<number> --> Neel_Query_1
    output_filename = "Name of your output file"
    #Name your index you want Elasticsearch
    # * = everything
    # geo = geo tweet
    # it will increase as per data
    # heatdata = heatmap geo enable per country
    # <----------------------------------------------------->
    index = '*'
    doc_type = 'tweet'
    query = { "query": query }
    page_size = 1000
    output = []
    for total_pages, page_counter, page_items, page_data in scroll(index, doc_type, query, page_size=page_size):
        print('total_pages={}, page_counter={}, page_items={}'.format(total_pages, page_counter, page_items))
        print(page_data)
        print("\n ---------------------------------- \n")
        output.append(page_data)

    try:
        with open("/home/nshah5/"+str(output_filename)+".json","w") as f:
            json.dump(output, f, sort_keys=True, indent=4)
    except Exception as e:
        print("Error "+str(e))

    return None

if __name__=="__main__":
    main()
    print("Done!!! --> Check your file at /home/nshah5/<name of your file>.json")
