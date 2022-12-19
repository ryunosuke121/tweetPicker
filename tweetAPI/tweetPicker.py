import requests
import json

def create_url(query, tweet_fields, max_results):
    if(any(tweet_fields)):
        formatted_tweet_fields = "tweet.fields=" + ",".join(tweet_fields)
    else:
         formatted_tweet_fields = ""
    formatted_max_results = "max_results=" + max_results
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}&{}".format(
        query, formatted_tweet_fields, formatted_max_results
    )
    return url

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main(tweetID):
    # bearer_token = auth()
    BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAAF5qkQEAAAAAzexLIeNvh4xvbfRxiVjpmTx0Rwg%3DpNllmERsJjVP9fGfxgACXOMBLi5DEP9By0IgbnGdeUQhlQozkz"
    query = "conversation_id:" + str(tweetID)
    # 検索ワード  e.g. query = "テスト" / query = "テスト OR test"
    # OR 検索　AND検索　-検索　などしたい場合はそのように書く
    tweet_fields = ["created_at", "author_id", "conversation_id"]
    # 取得データ  e.g. tweet_fields = ["created_at", "author_id"]
    max_results = '100'
    # 空の場合は ツイートのid, text のみ取得する。
    # created_at(投稿時刻), author_id(アカウントID)などの情報が欲しい場合はtweet_fieldsに書く
    url = create_url(query, tweet_fields, max_results)
    headers = create_headers(BEARER_TOKEN)
    json_response = connect_to_endpoint(url, headers)
    tweet_texts = []
    for tweet in json_response["data"]:
            tweet_texts.append(tweet['text'])
    #print(newData)
    #result_text = json.dumps(tweet_texts, indent=4, sort_keys=True, ensure_ascii=False)
    #print(result_text)
    return tweet_texts