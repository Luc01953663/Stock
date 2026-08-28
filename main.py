from stock import Stocks,Display,find_percent,get_stocks_name
from text  import create_message
from new import get_new
from email_sender import send_email

def main():
    stocks = int(input("how many stocks do you want to keep track of").strip())
    get_stock_data = get_stocks_name(stocks) #JUST THE STOCKS
    gets_new = Stocks(get_stock_data) # ALL THE STOCK DATA
    the_news = get_new(get_stock_data)
    send_email(the_news)  
    
    
    new_data = get_new(get_stock_data)
    create_message(the_news)
    
    Display(find_percent())
    pass

if __name__ == "__main__":
    main()