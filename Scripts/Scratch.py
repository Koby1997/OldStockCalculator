import yfinance as yf
import pandas as pd
import time

# Define a list of stock tickers
stock_tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

start_time = time.time()
# Retrieve all available historical data for each stock in the list
stock_data = yf.download(stock_tickers)
end_time = time.time()
print("Total time = ", end_time - start_time)


print(stock_data.columns)

s = time.time()
apple = yf.Ticker("AAPL")
apple_data = apple.history(period="max")
e = time.time()
print("YO:   ", e - s)



print("Check")
print(apple_data)

