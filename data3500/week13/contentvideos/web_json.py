import requests
import json
import time
    
ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'

# http://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8


adj_closed_key = "5. adjusted close"
time_series_key = "Time Series (Daily)"

stock_txt = requests.get(url).text

stock_dct = json.loads(stock_txt)


# print(stock_dct)

for day_key in stock_dct[time_series_key]:
    print(stock_dct[time_series_key][day_key][adj_closed_key])
    time.sleep(12)

    
    
    
    
    
    
    
    
    


