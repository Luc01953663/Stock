import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

api_key = os.getenv("INVEST_API")
print(repr(api_key))
stock_data = {} # list of close 
final_data = {} # list of close result


def Stocks(num):
    #num2 = num
    stock = num
    try:
        for i in stock:
            params = {
                "function": "TIME_SERIES_DAILY",
                "symbol": i,
                "apikey": api_key
            }
            r = requests.get("https://www.alphavantage.co/query", params=params)
            r.raise_for_status()
            data = r.json()
            if 'Time Series (Daily)' not in data:
                print("not in data")
            print(data)
            dates = sorted(data['Time Series (Daily)'].keys())
            most_recent = dates[-1]
            second_most = dates[-2]
            stock_data[i] = {
                "today": data['Time Series (Daily)'][most_recent]['4. close'],
                "yesterday": data['Time Series (Daily)'][second_most]['4. close']
            }
            time.sleep(2)         
            print(data)
        return data 
    except requests.exceptions as e:
        print("Something went wrong",e)
        return
        

def get_stocks_name(num): # return a list of name
    
    stocks = []
    for i in range(num):
        stocks.append(input("Give me a stock: ").strip()) 
    return stocks

def find_percent():
    total_percent = None
    total = None
    for i in stock_data:
        total = (float(stock_data[i]["today"]) - float (stock_data[i]["yesterday"]))
        total_percent = (total / (float (stock_data[i]["yesterday"]))) * 100
        final_data[i] = {
            "Difference": total,
            "Percent": total_percent
        }
    return final_data

def Display(list):
    print(list)