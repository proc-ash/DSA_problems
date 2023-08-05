# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
# to sell that stock. Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

def buySell(stocks):
    buy_day = 0
    sell_day = 1
    profit = 0
    while sell_day <len(stocks):
        if stocks[buy_day]< stocks[sell_day]:
            #print(stocks[sell_day], stocks[buy_day])
            profit = max(profit, stocks[sell_day]-stocks[buy_day])
            #print(profit)
        if sell_day == len(stocks) -1:
            buy_day += 1
            sell_day = buy_day
        sell_day +=1
    return profit

if __name__ =='__main__':
    array = [7,1,5,3,6,4]
    print(buySell(array))

