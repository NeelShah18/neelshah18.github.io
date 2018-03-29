import json
import elasticsearch
import abc

def main():
    temp_dic = {}
    es = elasticsearch.Elasticsearch()
    i = 1
    with open('Aug13.json','r') as f:
        for line in f:
            one_dic = json.loads(line)
            if(one_dic["tweet_data"]["geo"] != None):
                temp1 = True
            else:
                temp1= False
            if(one_dic["tweet_data"]["place"] != None):
                temp2 = True
            else:
                temp2 = False
            try:
                if(one_dic["tweet_data"]["user"]["listed_count"] != None):
                    temp3 = one_dic["tweet_data"]["user"]["listed_count"]
                else:
                    temp3 = "False"
            except:
                temp3 = "False"
            try:
                if(one_dic["tweet_data"]["user"]["profile_banner_url"] != None):
                    temp4 = one_dic["tweet_data"]["user"]["profile_banner_url"]
                else:
                    temp4 = "False"
            except:
                temp4 = "False"

            temp_dic={
            "unique_id": one_dic["_id"],
            "created_at": one_dic["created_at"],
            "favourite_count": one_dic["tweet_data"]["favorite_count"],
            "favorited": one_dic["tweet_data"]["favorited"],
            "geo_tag": temp1,
            "tweet_id": one_dic["tweet_data"]["id"]["$numberLong"],
            "language": one_dic["tweet_data"]["lang"],
            "palce": temp2,
            "is_quote_status": one_dic["tweet_data"]["is_quote_status"],
            "in_reply_to_screen_name": one_dic["tweet_data"]["in_reply_to_screen_name"],
            "in_reply_to_status_id": one_dic["tweet_data"]["in_reply_to_status_id"],
            "favorite_count": one_dic["tweet_data"]["favorite_count"],
            "favorited": one_dic["tweet_data"]["favorited"],
            "filter_level": one_dic["tweet_data"]["filter_level"],
            "place_tag": one_dic["tweet_data"]["place"],
            "retweet_count": one_dic["tweet_data"]["retweet_count"],
            "retweeted": one_dic["tweet_data"]["retweeted"],
            "source": one_dic["tweet_data"]["source"],
            "text": one_dic["tweet_data"]["text"],
            "truncated": one_dic["tweet_data"]["truncated"],
            "contributors_enabled": one_dic["tweet_data"]["user"]["contributors_enabled"],
            "user_created_at": one_dic["tweet_data"]["user"]["created_at"],
            "user_default_profile": one_dic["tweet_data"]["user"]["default_profile"],
            "user_description": one_dic["tweet_data"]["user"]["description"],
            "user_favourites_count": one_dic["tweet_data"]["user"]["favourites_count"],
            "user_followers_count": one_dic["tweet_data"]["user"]["followers_count"],
            "user_follow_request_sent": one_dic["tweet_data"]["user"]["follow_request_sent"],
            "user_friends_count": one_dic["tweet_data"]["user"]["friends_count"],
            "user_geo_enabled": one_dic["tweet_data"]["user"]["geo_enabled"],
            "user_is_translator": one_dic["tweet_data"]["user"]["is_translator"],
            "user_lang": one_dic["tweet_data"]["user"]["lang"],
            "user_listed_count": temp3,
            "user_location": one_dic["tweet_data"]["user"]["location"],
            "user_name": one_dic["tweet_data"]["user"]["name"],
            "user_profile_banner_url": temp4,
            "user_prfile_image_url": one_dic["tweet_data"]["user"]["profile_image_url"],
            "user_protected": one_dic["tweet_data"]["user"]["protected"],
            "user_screen_name": one_dic["tweet_data"]["user"]["screen_name"],
            "user_statuses_count": one_dic["tweet_data"]["user"]["statuses_count"],
            "user_time_zone": one_dic["tweet_data"]["user"]["time_zone"],
            "user_url": one_dic["tweet_data"]["user"]["url"],
            "user_utc_offset": one_dic["tweet_data"]["user"]["utc_offset"],
            "user_verified": one_dic["tweet_data"]["user"]["verified"],
            "user_retweet_count": one_dic["tweet_data"]["retweet_count"]
            }
            es.index(index='tindex1', doc_type='tmap1', id=i, body=temp_dic)
            i = i+1
            print(i)
            #print(json.dumps(temp_dic, sort_keys=True, indent=4, separators=(',',':')))
    f.close()
    return None

if __name__=="__main__":
    main()
