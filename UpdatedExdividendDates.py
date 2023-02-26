import yfinance as yf
import datetime
from StockClass import Stock


# List of tickers to make
stock_symbols = ["AAPL","AAPL"]#,"GOOGL","MSFT","JPM","JNJ","V","BABA","WMT","PG","NFLX","DIS"]
stock_list = []


#Create all stock objects now
for symbol in stock_symbols:
    stock = Stock(symbol)
    stock_list.append(stock)
        

with open('output.txt', 'w') as f:

    keep_count = 1
    #loop through all stocks listed above
    for stock in stock_list:
        # Print the list of all available stock tickers
        try:
            print("well check this first")
            print(stock.symbol)
            current_stock_ticker = yf.Ticker(stock.symbol)
            print("new stock ticker")
        except ValueError:
            print("Could not find data for symbol: " + stock.symbol)
            continue

        print("info ", current_stock_ticker.actions)

        dividends = current_stock_ticker.dividends
        # print(dividends)
        # Get all of the ex-dividend dates
        ex_dividend_dates = dividends.index.to_pydatetime()
        # print(ex_dividend_dates)

        


        for buy_date in range(5,7):# range(4,21):

            for sell_day in range(-2,0):#(-3, 3):

                for date in ex_dividend_dates:

                    #important to remember that our list goes from [curent, past, ->]
                    #so the further in the array we go, the further back we go
                    #but then adding a day to a date is different. adding a day goes into the future
                    buy_date_dt = datetime.timedelta(days=buy_date)
                    sell_day_dt = datetime.timedelta(days=sell_day)
                    one_day_dt = datetime.timedelta(days=1)

                    if current_stock_ticker.history(start=(date - buy_date_dt - one_day_dt), end=(date - sell_day_dt)).empty:
                        print("Error: Skipping because no data. Not adding to the calculations\n")
                        continue


                    data = current_stock_ticker.history(start=(date - buy_date_dt - one_day_dt), end=(date - sell_day_dt))
                    # print(data)
                    price_difference = data['Open'][len(data['Open']) - 1] - data['Close'][0] #want positive? positive means stock went up. sell date - buy date
                    stock.single_price_change.append(price_difference)

                    percent_change = (((data['Open'][len(data['Open']) - 1] - data['Close'][0]) / data['Close'][0]) * 100)
                    #    ((Sell - buy)/buy) * 100
                    stock.single_perc_change.append(percent_change)


                print("Calculations for ", stock.symbol, "with buy day: ", buy_date, " and sell date: ", sell_day, file=f)
                print("Average price Difference: ", stock.calculate_avg_single_price_change(), file=f)
                print("Average of the actual percentage rise/drop between the ", sell_day, " days before earning day and ", buy_date, " days after: ", stock.calculate_avg_single_perc_change(), "%", file=f)
                # print("Percentage of times that the stock price went down: ", percent_total_went_down, "%", file=f)
                print(stock.symbol + " Single date range complete\n", file=f)

                stock.clean_single_data()
                print("Done for ", buy_date, " ", sell_day)

        print("Done with stock: ", stock.symbol)
        print((keep_count / 12) * 100, " o/o complete")

            

    print("fully done with going through the date ranges")

    final_avg_price_change = []
    final_avg_perc_change = []

    first = 0

    for stock in stock_list:
        if first == 0:
            final_avg_price_change = stock.multiple_price_change.copy()
            final_avg_perc_change = stock.multiple_perc_change.copy()
            first = 1
            continue


        for i in range(len(final_avg_price_change)):
            final_avg_price_change[i] = (final_avg_price_change[i] + stock.multiple_price_change[i]) / 2
            final_avg_perc_change[i] = (final_avg_perc_change[i] + stock.multiple_perc_change[i]) / 2

        for i in range(len(final_avg_price_change)):
            print("Date range ", i, file=f)
            print("Average Price change for all stocks in this date range: ", final_avg_price_change[1], file=f)
            print("Average Percentage change for all stocks in this date range: ", final_avg_perc_change[1], "%", file=f)


    print("wow", file=f)