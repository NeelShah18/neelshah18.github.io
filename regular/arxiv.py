import urllib.request
import feedparser
import time

# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
search_query = 'cat:cs.CV+OR+cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL+OR+cat:cs.NE+OR+cat:stat.ML' # search for CV,CL,AI,LG,NE,ML field papers
start = 0
# retreive the first 1000 results
max_results = 1000
count = 0
fail_count = 0
lol_count= 0
while start < 24000:
    time.sleep(5)
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query,start,max_results)
    start = start + 1000

    # Opensearch metadata such as totalResults, startIndex,
    # and itemsPerPage live in the opensearch namespase.
    # Some entry metadata lives in the arXiv namespace.
    # This is a hack to expose both of these namespaces in
    # feedparser v4.1
    feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
    feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'

    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)

    # print out feed information
    print('Feed title: %s' % feed.feed.title)
    print('Feed last updated: %s' % feed.feed.updated)

    # print opensearch metadata
    # print('totalResults for this query: %s' % feed.feed.opensearch_totalresults)
    # print('itemsPerPage for this query: %s' % feed.feed.opensearch_itemsperpage)
    # print('startIndex for this query: %s'   % feed.feed.opensearch_startindex)

    # Run through each entry, and print out information
    for entry in feed.entries:
        print('e-print metadata')
        print('arxiv-id: %s' % entry.id.split('/abs/')[-1])
        c1_data = "'"+str(entry.id.split('/abs/')[-1])+"'"
        print('Published: %s' % entry.published)
        c2_data = "'"+str(entry.published)+"'"
        year = int(str(c2_data[1:5]))
        month = int(str(c2_data[6:8]))
        if(year==2018 and month<4):
            lol_count=lol_count+1
        try:

            print(lol_count)
            count += 1
        except:
            fail_count += 1
            pass


print('Final count: '+lol_count)
print('Connection is closed!')
