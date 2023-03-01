import yfinance as yf
import numpy as np
import datetime


# # List of tickers to make
# all_tickers = [
#     "AAPL", "ABT", "ADBE", "AMAT", "AMGN",
#     "AXP", "BA", "BAC", "BLK", "BMY", "CAT", "CMCSA", "COST",
#     "CVS", "CVX", "DIS", "F", "GE", "GS",
#     "HD", "HON", "IBM", "JCI", "JNJ", "JPM", "KO", "LLY",
#     "LOW", "MA", "MDLZ", "MDT", "MMM", "MO", "MRK", "MSFT", "MU",
#     "NKE", "NEE", "ORCL", "PFE", "PG", "PM",
#     "QCOM", "RTX", "SLB", "SPG", "T", "TXN", "UNH",
#     "UNP", "UPS", "V", "VLO", "VZ", "WBA", "WFC", "WMT", "XOM"
# ] #64 Stocks
# ["PXD","MO","VZ","KMI","OKE","T","WBA","IP","PRU","PM","NEM","F","DOW","HAS","LYB","PNW","D","NRG","KEY","VFC","TFC","AMCR","AAP","IVZ","BBY"]



#["MO","VZ","OKE","T","WBA","IP","PM","NEM","F","HAS","PNW","D","KEY","VFC","TFC","AAP","IVZ","BBY"]

all_tickers = ["MO","VZ","OKE"]






count = 0



ticker_success_count = 0

#loop through all stocks listed above
for symbol in all_tickers:
    # Print the list of all available stock tickers
    try:
        stock = yf.Ticker(symbol)
    except ValueError:
        print("Could not find data for symbol: " + symbol)
        continue


    dividends = stock.dividends

    # Get all of the ex-dividend dates
    ex_dividend_dates = dividends.index.to_pydatetime()

    # # Print the ex-dividend dates
    # print(f"The ex-dividend dates for {symbol} are:")
    # for date in ex_dividend_dates:
    #     print(date)


    if len(ex_dividend_dates) > 0:
        print(symbol, "        good     ", len(ex_dividend_dates))
        count += len(ex_dividend_dates)
    else:
        print(symbol, " BAD")



print("total:     ", count)
