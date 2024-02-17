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

    print("This is the dividends: ")
    print(dividends)

    try:
        Xdates = dividends.index.to_pydatetime()

        print("Xdates: ")
        print(Xdates)
    except:
        print("Dividends didn't work, delete ", stock)
        return False

    if len(Xdates) <= 40:
        print("Not enough data points for ", stock, " . Data points: ", len(Xdates))
        return False
    

    print("                                                                   ", stock, "  PASSED ALL TESTS WITH ", len(Xdates), " DATA POINTS.")
    return True




# Read stocks from file
with open("temp.txt", "r") as file:
    stocks = file.read().splitlines()


stocks_with_data = [stock for stock in stocks if check_stock_info(stock)]