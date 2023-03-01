import yfinance as yf
import numpy as np
import datetime


with open('output.txt', 'w') as f:







    largest_tot_avg = 0
    largest_tot_perc = 0
    largest_tot_perc_change = 0






    for i in range(4,21):
        temp_tot_avg = 0
        temp_tot_perc = 0
        temp_tot_perc_change = 0
        for j in range(-3, 3):



            # List of tickers to make
            all_tickers = ["AAPL","AMZN","GOOGL","MSFT","JPM","JNJ","V","BABA","WMT","PG","NFLX","DIS"]
            ticker_success_count = 0



            all_stock_price_difference = 0
            all_stock_percent_total_went_down = 0
            all_stock_percent_change = 0


            # days_back = int(input("How many days before the Earnings day would you buy? "))
            # print(days_back)

            # sell_day = int(input("How many days before the earnings day would you sell? (Negative numbers would be after the Earnings day) "))
            # print(sell_day)

            days_back = i
            sell_day = j

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
                print(dates)

                #important to remember that our list goes from [curent, past, ->]
                #so the further in the array we go, the further back we go
                #but then adding a day to a date is different. adding a day goes into the future

                days_back_dt = datetime.timedelta(days=days_back)
                sell_day_dt = datetime.timedelta(days=sell_day)
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

                    buy_date = date - days_back_dt - one_day_dt
                    sell_date = date - sell_day_dt

                    print("Buy date:  ", buy_date)
                    print("Sell date: ", sell_date)
                    print("Earnings date: ", date)
                
                    if stock.history(start=(date - days_back_dt - one_day_dt), end=(date - sell_day_dt)).empty:
                        print("Error: Skipping because no data. Not adding to the calculations\n")
                        continue

                    non_error_dates += 1

                    data = stock.history(start=(date - days_back_dt - one_day_dt), end=(date - sell_day_dt))
                    # print(data)
                    price_difference = data['Open'][len(data['Open']) - 1] - data['Close'][0] #want positive? positive means stock went up. earnings date - days before
                    individual_stock_price_difference += price_difference

                    individual_stock_percent_change += (((data['Open'][len(data['Open']) - 1] - data['Close'][0]) / data['Close'][0]) * 100)
                    #    ((Sell - buy)/buy) * 100
                    

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

                print("Calculations for ", symbol, "with buy day: ", i, " and sell date: ", j) #, file=f)
                print("Average price Difference: ", average_price_difference) #, file=f)
                print("Average of the actual percentage rise/drop between the ", sell_day, " days before earning day and ", days_back, " days after: ", individual_stock_percent_change, "%") #, file=f)
                print("Percentage of times that the stock price went down: ", percent_total_went_down, "%") #, file=f)
                

                print(symbol + " Complete\n") #, file=f)




            tot_avg = all_stock_price_difference / ticker_success_count
            tot_perc = all_stock_percent_total_went_down / ticker_success_count
            tot_perc_change = all_stock_percent_change / ticker_success_count

            print("Buy date: ", days_back, " days before Earnings day. Sell date: ", sell_day, " days before Earnings day") #, file=f)
            # print("Average stock price difference of all stocks when comparing ", days_back, " days before earnings day:  ", tot_avg)
            # print("Average of the actual percentage rize/drop when bought ", days_back, " days before earnings day and sold ", sell_day, " days before earnings day: ", tot_perc_change, "%")
            # print("Average percent of all stocks that decreased (no matter the amount) over the time period:  ", tot_perc, "%")

            print(tot_avg) #, file=f)
            print(tot_perc_change, "%") #, file=f)
            print(tot_perc, "%\n") #, file=f)

            if tot_avg > temp_tot_avg:
                temp_tot_avg = tot_avg

            if tot_perc_change > temp_tot_perc_change:
                temp_tot_perc_change = tot_perc_change

            if tot_perc > temp_tot_perc:
                temp_tot_perc = tot_perc

        if temp_tot_avg > largest_tot_avg:
            largest_tot_avg = temp_tot_avg

        if temp_tot_perc_change > largest_tot_perc_change:
            largest_tot_perc_change = temp_tot_perc_change

        if temp_tot_perc > largest_tot_perc:
            largest_tot_perc = temp_tot_perc


    print("Fully done. Here are the largest datapoint:", file=f)
    print(largest_tot_avg, file=f)
    print(largest_tot_perc_change, file=f)
    print(largest_tot_perc, file=f)


    print("wow", file=f)