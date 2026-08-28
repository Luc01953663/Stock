import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
news_api = os.getenv("NEWS_API") 
def get_new(Dict):
    news_data = {}
    for i in Dict:
        params = {
            "q": i,
            "apikey": news_api,
            "sortby": "relevancy",
            "language": "en"
        }
        r = requests.get("https://newsapi.org/v2/everything",params=params)
        data = r.json()
        new_data = {
        "author":data["articles"][0]["author"],
        "title":data["articles"][0]["title"],
        "description":data["articles"][0]["description"],
        "url":data["articles"][0]["url"],
        "source":data["articles"][0]["urlToImage"],
        "publishedAt":data["articles"][0]["publishedAt"],
        "content":data["articles"][0]["content"]
        }
        news_data[i] = new_data
        time.sleep(2)   
        #return a lisit for message
    return news_data
        #put a sleep