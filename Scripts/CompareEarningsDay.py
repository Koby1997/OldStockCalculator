import yfinance as yf
import numpy as np
import datetime


# List of tickers to make
all_tickers = ["AAPL","AMZN","GOOGL","MSFT","JPM","JNJ","V","BABA","WMT","PG","NFLX","DIS"]
ticker_success_count = 0



all_stock_price_difference = 0
all_stock_percent_total_went_down = 0
all_stock_percent_change = 0

#loop through all stocks listed above
for symbol in all_tickers:
    # Print the list of all available stock tickers
    try:
        stock = yf.Ticker(symbol)
    except ValueError:
        print("Could not find data for symbol: " + symbol)
        continue


    # Print the earnings call dates
    earnings_call_dates_and_data = stock.get_earnings_dates(limit=150)
    # print(earnings_call_dates_and_data)

    # gives a DatetimeIndex which cannot be used with .timedelta
    earnings_call_dates = earnings_call_dates_and_data.index

    # change format to datetime to allow the used of .timedelta
    dates = earnings_call_dates.to_pydatetime()
    #There are multiple future dates added. So we want to get rid of those
    dates = dates[10:]

    #important to remember that our list goes from [curent, past, ->]
    #so the further in the array we go, the further back we go
    #but then adding a day to a date is different. adding a day goes into the future

    one_day = datetime.timedelta(days=1)


    # print("Day")
    # print(dates[4])
    # print("Adding day") #go into future
    # print(dates[4] + one_day)
    # print("Subtracting a day") #go into past
    # print(dates[4] - one_day)


    # Gets data for a stock on a day "10"
    # data = stock.history(start=(dates[10]) , end=(dates[10] + one_day))


    how_many_went_down = 0
    total_price_difference = 0
    individual_stock_percent_change = 0
    non_error_dates = 0

    for date in dates:
    
        if stock.history(start=(date), end=(date + one_day)).empty:
            print("Error: Skipping because no data. Not adding to the calculations\n")
            continue

        non_error_dates += 1

        data = stock.history(start=(date ), end=(date + one_day))
        # print(data)
        price_difference = data['Close'][0] - data['Open'][0]
        total_price_difference += price_difference

        individual_stock_percent_change += (((data['Close'][0] - data['Open'][0]) / data['Open'][0]) * 100)
        

        if(price_difference < 0 ):
            #higher at beginning of the day, therefore it went down. This is expected
            how_many_went_down += 1


    average_price_difference = total_price_difference / non_error_dates
    all_stock_price_difference += average_price_difference

    percent_total_went_down = (how_many_went_down / non_error_dates) * 100
    all_stock_percent_total_went_down += percent_total_went_down

    all_stock_percent_change += individual_stock_percent_change / non_error_dates

    ticker_success_count += 1

    print("Calculations for ", symbol)
    print("Average price Difference: ", average_price_difference)
    print("Average of the actual percentage rise/drop on the day of Earnings: ", all_stock_percent_change, "%")
    print("Percent that went down: ", percent_total_went_down, "%")
    

    print(symbol + " Complete\n")




tot_avg = all_stock_price_difference / ticker_success_count
tot_perc = all_stock_percent_total_went_down / ticker_success_count
tot_perc_change = all_stock_percent_change / ticker_success_count

print("I don't know if this is a good final, would have to check the math but")
print("Average stock price difference from open to close of all stocks:   ", tot_avg)
print("Average of the actual percentage rize/drop on the day of Earnings for all stocks: ", tot_perc_change)
print("Average percent of Earning days where the closing price was LOWER than the opening price   ", tot_perc, "%")