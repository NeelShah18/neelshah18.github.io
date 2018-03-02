import json

def main():
    i = 0
    with open('Aug13.json','r') as f:
        for line in f:
            one_dic = json.loads(line)
            '''
            ["_id"]
            ["created_at"]
            ["tweet_data"]["favorite_count"]
            ["tweet_data"]["favorited"]
            ["tweet_data"]["geo"]// true or false
            ["tweet_data"]["id"]["$numberLong"]
            ["tweet_data"]["lang"]
            ["tweet_data"]["place"]//true or false
            ["tweet_data"]["is_quote_status"]
            ["tweet_data"]["in_reply_to_screen_name"]
            ["tweet_data"]["in_reply_to_status_id"]
            ["tweet_data"]["possibly_sensitive"]
            ["tweet_data"]["entities"] //-->
            ["tweet_data"]["quoted_status"]["entities"]
            ["tweet_data"]["favorite_count"]
            ["tweet_data"]["favorited"]
            ["tweet_data"]["filter_level"]
            ["tweet_data"]["geo"]
            ["tweet_data"]["place"]
            ["tweet_data"]["retweet_count"]
            ["tweet_data"]["retweeted"]
            ["tweet_data"]["source"]
            ["tweet_data"]["text"]
            ["tweet_data"]["truncated"]
            ["tweet_data"]["user"]["contributors_enabled"]
            ["tweet_data"]["user"]["created_at"]
            ["tweet_data"]["user"]["default_profile"]
            ["tweet_data"]["user"]["description"]
            ["tweet_data"]["user"]["favourites_count"]
            ["tweet_data"]["user"]["followers_count"]
            ["tweet_data"]["user"]["follow_request_sent"]
            ["tweet_data"]["user"]["friends_count"]
            ["tweet_data"]["user"]["geo_enabled"]
            ["tweet_data"]["user"]["is_translator"]
            ["tweet_data"]["user"]["lang"]
            ["tweet_data"]["user"]["listed_count"]
            ["tweet_data"]["user"]["location"]
            ["tweet_data"]["user"]["name"]
            ["tweet_data"]["user"]["profile_image_url"]
            ["tweet_data"]["user"]["profile_banner_url"]
            ["tweet_data"]["user"]["protected"]
            ["tweet_data"]["user"]["screen_name"]
            ["tweet_data"]["user"]["statuses_count"]
            ["tweet_data"]["user"]["time_zone"]
            ["tweet_data"]["user"]["url"]
            ["tweet_data"]["user"]["utc_offset"]
            ["tweet_data"]["user"]["verified"]
            ["tweet_data"]["retweet_count"]
            '''
            print(json.dumps(one_dic, sort_keys=True, indent=4, separators=(',',':')))
            break
    f.close()
    return None

if __name__=="__main__":
    main()
