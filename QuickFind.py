import yfinance as yf
import numpy as np
import datetime


# List of tickers to make
all_tickers = ["GE", "AAPL", "AMZN","GOOGL","MSFT","JPM","JNJ","V","BABA","WMT","PG","NFLX","DIS"]
ticker_success_count = 0

#loop through all stocks listed above
for symbol in all_tickers:
    # Print the list of all available stock tickers
    try:
        stock = yf.Ticker(symbol)
    except ValueError:
        print("Could not find data for symbol: " + symbol)
        continue


    # earnings_call_dates_and_data = stock.get_earnings_dates(limit=150)
    # # print(earnings_call_dates_and_data)

    # # gives a DatetimeIndex which cannot be used with .timedelta
    # earnings_call_dates = earnings_call_dates_and_data.index

    # # change format to datetime to allow the used of .timedelta
    # dates = earnings_call_dates.to_pydatetime()



    dividends = stock.dividends

    # Get all of the ex-dividend dates
    ex_dividend_dates = dividends.index.to_pydatetime()

    # # Print the ex-dividend dates
    # print(f"The ex-dividend dates for {symbol} are:")
    # for date in ex_dividend_dates:
    #     print(date)

    if len(ex_dividend_dates) > 0:
        print(symbol, "        good")
    else:
        print(symbol, " BAD")

