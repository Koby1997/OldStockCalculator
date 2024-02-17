# Print out the info for these stocks. Can be helpful to see what info we can use

import yfinance as yf


ticker_symbols = ['AAPL', 'MSFT', 'GOOG']

# Initialize the Tickers object with the list of ticker symbols
all_tickers = yf.Tickers(ticker_symbols)
print("What even is this????   :   ")
print(all_tickers)
print("DOne")

# Now you can access data for each ticker symbol individually
for ticker_symbol in ticker_symbols:
    ticker = all_tickers.tickers[ticker_symbol]
    print(f"Symbol: {ticker_symbol}, Name: {ticker.info['longName']}")
    print("Info:")
    for key, value in ticker.info.items():
        print(f"{key}: {value}")
    print("\n")
