import json

print("hello")


def simpleMovingAverageStrategy(prices):
    total_profit = 0.0
    i = 0
    buy = 0
    for price in prices:
        if i >= 4: # 4 day moving average
            avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] ) / 4
            # print("avg: ", avg)
            if price > avg and buy == 0:
                print("buying at: ", price)
                buy = price
            elif price < avg and buy != 0:
                print("selling at: ", price)
                total_profit += price - buy
                buy = 0
            else:
                pass #do nothing
            
        i += 1
        
    returns = total_profit / prices[0] # i am not using a first buy, but you will on your hw
    
    return total_profit, returns
    

tickers = ["AAPL", "GOOG", "CCL"]
results = {}
for ticker in tickers:
    f = open("/home/ubuntu/environment/data3500_spring2023/data3500/week10/review_activities2/" + ticker + ".txt", "r")
    lines = f.readlines()
    print("lines: ", lines)
    
    prices = []
    for line in lines:
        prices.append(float(line))
    results[ticker + "_prices"] = prices
    # print("prices: ", prices)
    
    # call the strategy
    profit, returns = simpleMovingAverageStrategy(prices)
    results[ticker + "_sma_profit"] = profit
    results[ticker + "_sma_returns"] = returns

json.dump(results, open("/home/ubuntu/environment/results.json", "w"), indent=4)