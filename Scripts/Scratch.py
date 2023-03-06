import yfinance as yf
import pandas as pd
import time
import datetime

pd.set_option('display.max_rows', None)


data = yf.download("AAPL")

# print(data)
print("\n Ok some spaces \n \n \n \n")



weekends = pd.date_range(start=data.index.min(), end=data.index.max(), freq='W-SAT')
print("W1")
print(weekends)

# Add Sundays to the weekends DataFrame
weekends = weekends.union(pd.date_range(start=data.index.min(), end=data.index.max(), freq='W-SUN'))
print("W2222222222")
print(weekends)
# Create a new DataFrame with only the weekend data
weekend_data = data.reindex(weekends)
print(weekend_data)

# Forward-fill the missing values for the weekend data
# weekend_data = weekend_data.ffill()
print("What is this?")
# print(weekend_data)

# Combine the original data with the weekend data
data = data.combine_first(weekend_data)
# print(data)

data = data.bfill()
print(data)



# # Resample data to daily frequency
# data = data.resample('D').ffill()


# print(data)

# Fill in missing values for weekends or any other missing dates
# data = data.asfreq('D', method='ffill')

# print(data)








# # Define a list of stock tickers
# stock_tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'AAPL']

# for stock in stock_tickers:
#     # Retrieve all available historical data for each stock in the list
#     stock_data = yf.download(stock)
#     current_stock_ticker = yf.Ticker(stock)

#     dividends = current_stock_ticker.dividends
#     #change to python list of timezone-naive objects
#     ex_dividend_dates = dividends.index.tz_localize(None).to_pydatetime()


#     print(stock_data)

    # one_day_dt = datetime.timedelta(days=1)

    # for date in ex_dividend_dates:
    #     try:

    #         # print("date:  ", date)
    #         # print("date - 1  :  ", date - one_day_dt)
    #         value = stock_data.loc[date]
    #         # day_before = stock_data.loc[date - one_day_dt, 'Open']
    #         print("Value: ", value)
    #         # print("day before:   ", day_before)
    #     except:
    #         print("no value for that date")




