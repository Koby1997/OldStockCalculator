import yfinance as yf
import numpy as np
import datetime
from StockClass import Stock


stock_symbols = ["AHT","AKR","AMT","ARE","ARR","AVB","AVD","BXP","CLDT","CMCT","CUZ","CXW","DHC","DLR","EARN","ECL","EPR","EQR","ESS","EXR","FR","GOOD","HT","IRM","IRT","KIM","KRG","LAND","LXP","LSI","LTC","MAA","MLM","MPW","NEM","NEU","NNN","NLY","NHI","NUE","NYMT","O","OLP","PCH","PEAK","PLD","PPG","PSA","REG","RHP","SBRA","SCCO","SLG","SPG","SRC","SUI","STWD","UDR","UMH","VNO","VMC","VTR","WELL","WPC","WY",]
stock_list = []

for symbol in stock_symbols:
    stock = Stock(symbol)
    stock_list.append(stock)


count = 0

ticker_success_count = 0

final_list = []

#loop through all stocks listed above
for stock in stock_list:
    # Print the list of all available stock tickers
    try:
        current_stock_ticker = yf.Ticker(stock.symbol)
    except ValueError:
        print("Could not find data for symbol: " + stock)
        continue

    dividends = current_stock_ticker.dividends
    # Get all of the ex-dividend dates
    try:

        ex_dividend_dates = dividends.index.to_pydatetime()
    except:
        print("didn't work, delete ", stock.symbol)
        continue

    # # Print the ex-dividend dates
    # print(f"The ex-dividend dates for {stock} are:")
    # for date in ex_dividend_dates:
    #     print(date)


    if len(ex_dividend_dates) > 40:
        print(stock.symbol, "        good     ", len(ex_dividend_dates))
        final_list.append(stock)
        count += len(ex_dividend_dates)
    else:
        print(stock.symbol, " BAD")

print("total:     ", count)


#copy this output to work with any script. Remember to delete the last comma
print("[", end="")
for stock in final_list:
    print("\"", stock.symbol, "\",", end="")
print("]", end="")


