########### Print out a histogram

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import skew, kurtosis

# # Example array of stock percentage increase or decrease
# data = np.random.normal(loc=0, scale=1, size=100)  # Example data, replace with your actual data

# # Calculate standard deviation, skewness, and kurtosis
# std_dev = np.std(data)
# skewness = skew(data)
# kurt = kurtosis(data)

# print("Standard Deviation:", std_dev)
# print("Skewness:", skewness)
# print("Kurtosis:", kurt)

# # Create a histogram
# plt.hist(data, bins=20, edgecolor='black')
# plt.xlabel('Percentage Increase/Decrease')
# plt.ylabel('Frequency')
# plt.title('Distribution of Stock Percentage Increase/Decrease')
# plt.grid(True)
# plt.show()




import yfinance as yf
import warnings
from Classes.Stock import Stock

# Suppress FutureWarning from yfinance
warnings.filterwarnings("ignore", category=FutureWarning)


ticker_symbols = ['AAPL', 'MSFT', 'GOOG']

all_tickers = yf.Tickers(ticker_symbols)

for ticker_symbol in ticker_symbols:
    current_stock = Stock(ticker_symbol)



for i in range(10, 13):



    for j in range(1, 3):

        all_tickers = ['AAPL', 'MSFT', 'GOOG']

        days_back = i
        sell_day = j

        for symbol in all_tickers:

            try:
                stock = yf.Ticker(symbol)
            except ValueError:
                print("Could not find data for symbol: ", symbol)
                continue

            