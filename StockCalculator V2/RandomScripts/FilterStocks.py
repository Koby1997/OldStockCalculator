#This script filters from a large list and takes just the stocks yfinance has with at least 40 ex-dividend dates
import yfinance as yf
import warnings

# Suppress FutureWarning from yfinance
warnings.filterwarnings("ignore", category=FutureWarning)

def check_stock_info(stock):

    try:
        current_stock_ticker = yf.Ticker(stock)
    except ValueError:
        print("Could not find data for symbol: ", stock)
        return False

    dividends = current_stock_ticker.dividends

    try:
        Xdates = dividends.index.to_pydatetime()
    except:
        print("Dividends didn't work, delete ", stock)
        return False

    if len(Xdates) <= 40:
        print("Not enough data points for ", stock, " . Data points: ", len(Xdates))
        return False
    

    print("                                                                   ", stock, "  PASSED ALL TESTS WITH ", len(Xdates), " DATA POINTS.")
    return True




# Read stocks from file
with open("StockList.txt", "r") as file:
    stocks = file.read().splitlines()

# Filter stocks that have information
stocks_with_data = [stock for stock in stocks if check_stock_info(stock)]

# Write filtered stocks to Results.txt
with open("Results.txt", "w") as file:
    for stock in stocks_with_data:
        file.write(stock + '\n')

print("Filtered stocks written to Results.txt")
