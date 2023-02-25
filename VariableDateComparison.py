import yfinance as yf
import numpy as np
import datetime


# List of tickers to make
all_tickers = ["AAPL","AMZN","GOOGL","MSFT","JPM","JNJ","V","BABA","WMT","PG","NFLX","DIS"]
ticker_success_count = 0



all_stock_price_difference = 0
all_stock_percent_total_went_down = 0
all_stock_percent_change = 0


days_back = int(input("How many days before the earnings date would you like to go back and check on? "))
print(days_back)

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
    # print(dates)

    #important to remember that our list goes from [curent, past, ->]
    #so the further in the array we go, the further back we go
    #but then adding a day to a date is different. adding a day goes into the future

    days_back_dt = datetime.timedelta(days=days_back)
    one_day_dt = datetime.timedelta(days=1)


    # print("Day")
    # print(dates[4])
    # print("Adding day") #go into future
    # print(dates[4] + one_day)
    # print("Subtracting a day") #go into past
    # print(dates[4] - one_day)


    # Gets data for a stock on a day "10"
    # data = stock.history(start=(dates[10]) , end=(dates[10] + one_day))


    how_many_went_down = 0
    individual_stock_price_difference = 0
    individual_stock_percent_change = 0
    non_error_dates = 0

    for date in dates:
    
        if stock.history(start=(date - days_back_dt), end=(date)).empty:
            print("Error: Skipping because no data. Not adding to the calculations\n")
            continue

        non_error_dates += 1

        data = stock.history(start=(date - days_back_dt - one_day_dt), end=(date))
        # print(data)
        price_difference = data['Open'][len(data['Open']) - 1] - data['Close'][0] #want positive? positive means stock went up. earnings date - days before
        individual_stock_price_difference += price_difference

        individual_stock_percent_change += (((data['Open'][len(data['Open']) - 1] - data['Close'][0]) / data['Close'][0]) * 100)
        

        if(price_difference < 0 ):
            #higher at beginning of the day, therefore it went down. This is expected
            how_many_went_down += 1


    average_price_difference = individual_stock_price_difference / non_error_dates
    all_stock_price_difference += average_price_difference

    percent_total_went_down = (how_many_went_down / non_error_dates) * 100
    all_stock_percent_total_went_down += percent_total_went_down

    individual_stock_percent_change = (individual_stock_percent_change / non_error_dates)
    all_stock_percent_change += individual_stock_percent_change


    ticker_success_count += 1

    print("Calculations for ", symbol)
    print("Average price Difference: ", average_price_difference)
    print("Average of the actual percentage rise/drop between the day of earnings and ", days_back, ":  ", individual_stock_percent_change, "%")
    print("Percentage of times that the stock price went down: ", percent_total_went_down, "%")
    

    print(symbol + " Complete\n")




tot_avg = all_stock_price_difference / ticker_success_count
tot_perc = all_stock_percent_total_went_down / ticker_success_count
tot_perc_change = all_stock_percent_change / ticker_success_count

print("I don't know if this is a good final, would have to check the math but")
print("Average stock price difference of all stocks when comparing ", days_back, " days before earnings day:  ", tot_avg)
print("Average of the actual percentage rize/drop on the day of Earnings for all stocks: ", tot_perc_change, "%")
print("Average percent of all stocks that decreased (no matter the amount) over the time period:  ", tot_perc, "%")