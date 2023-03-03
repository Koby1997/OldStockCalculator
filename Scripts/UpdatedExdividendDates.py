import yfinance as yf
import datetime
import pandas as pd
import os
from StockClass import Stock
from openpyxl import load_workbook
from openpyxl.styles import Font, Border, Side


#Excel settings
work_book = load_workbook('../Excel_Sheets/Data.xlsx')



# List of tickers to make
stock_symbols = ["GOOD","HT","IRM","IRT","KIM","KRG","LAND","LXP","LSI","LTC","MAA","MLM","MPW","NEM","NEU","NNN","NLY","NHI","NUE","NYMT","O","OLP","PCH","PEAK","PLD","PPG","PSA","REG","RHP","SBRA","SCCO","SLG","SPG","SRC","SUI","STWD","UDR","UMH","VNO","VMC","VTR","WELL","WPC","WY",]
stock_list = []


#Create all stock objects now
for symbol in stock_symbols:
    stock = Stock(symbol)
    stock_list.append(stock)
        

with open('output.txt', 'w') as f:

    keep_count = 1
    #loop through all stocks listed above
    #We use a copy because we may need to altar the actual list during the loop
    for stock in stock_list.copy():
    
    #We want to make the ticker used by yfinance to get the data
        try:
            current_stock_ticker = yf.Ticker(stock.symbol)
        except ValueError:
            print("Could not find data for symbol: " + stock.symbol)
            continue

        dividends = current_stock_ticker.dividends
        # print(dividends)
        # Get all of the ex-dividend dates
        ex_dividend_dates = dividends.index.to_pydatetime()
        # print(ex_dividend_dates)


        
        enough_data = True
        for buy_date in range(7,21 + 1):

            for sell_day in range(-3,3 + 1):
                data_points = 0

                for date in ex_dividend_dates:

                    #important to remember that our list goes from [curent, past, ->]
                    #so the further in the array we go, the further back we go
                    #but then adding a day to a date is different. adding a day goes into the future
                    buy_date_dt = datetime.timedelta(days=buy_date)
                    sell_day_dt = datetime.timedelta(days=sell_day)
                    one_day_dt = datetime.timedelta(days=1)

                    if current_stock_ticker.history(start=(date - buy_date_dt - one_day_dt), end=(date - sell_day_dt)).empty:
                        # print("Error: Skipping because no data. Not adding to the calculations\n")
                        continue
                    #count the data point because it made it past this check
                    data_points += 1


                    data = current_stock_ticker.history(start=(date - buy_date_dt - one_day_dt), end=(date - sell_day_dt))
                    # print(data)
                    price_difference = data['Open'][len(data['Open']) - 1] - data['Close'][0] #want positive? positive means stock went up. sell date - buy date
                    stock.single_price_change.append(price_difference)

                    percent_change = (((data['Open'][len(data['Open']) - 1] - data['Close'][0]) / data['Close'][0]) * 100)
                    #    ((Sell - buy)/buy) * 100
                    stock.single_perc_change.append(percent_change)

                #if less than 50 data points, we don't want to use it
                if data_points < 50:
                    enough_data = False
                    break
                #Still need to take it out of stock_list so it isn't used later when having no data
                    

                print("Calculations for ", stock.symbol, "with buy day: ", buy_date, " and sell date: ", sell_day, file=f)
                print("Average price Difference: ", stock.calculate_avg_single_price_change(), file=f)
                print("Average of the actual percentage rise/drop: ", stock.calculate_avg_single_perc_change(), "%", file=f)
                # print("Percentage of times that the stock price went down: ", percent_total_went_down, "%", file=f)
                print(stock.symbol + " Single date range complete\n", file=f)

                stock.clean_single_data()
                print("Done for ", buy_date, " ", sell_day, "     ", stock.symbol)


            if enough_data == False:
                break


        if enough_data == False:
            print(stock.symbol, "   Not enough data points, skipping in the calcualtions to not altar the average")
            print(stock_list)
            stock_list.remove(stock)
            print("I just removed the stock")
            print(stock_list)

        print("Done with stock: ", stock.symbol)
        print((keep_count / len(stock_symbols)) * 100, " o/o complete.     just did   ", keep_count)
        keep_count = keep_count + 1




        #We are done with the stock, so save its data to the Excel doc
        work_sheet = work_book.create_sheet(stock.symbol)

        # add row titles
        row_titles = ["7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]
        for i, title in enumerate(row_titles):
            work_sheet.cell(row=i+2, column=1, value=title).font = Font(bold=True)

        # add column titles
        col_titles = ["-3", "-2", "-1", "0", "1", "2", "3"]
        for i, title in enumerate(col_titles):
            work_sheet.cell(row=1, column=i+2, value=title).font = Font(bold=True)

        
        # write the data to the worksheet
        row = 2
        col = 2
        for value in stock.multiple_perc_change:
            work_sheet.cell(row=row, column=col, value=value)
            col += 1
            if col > 8:
                col = 2
                row += 1
        
        work_book.save('../Excel_Sheets/Data.xlsx')

            

    print("fully done with going through the date ranges")

    final_avg_price_change = []
    final_avg_perc_change = []

    first = 0

    for stock in stock_list:
        print("Each day-range percent average for ", stock.symbol, file=f)

        if first == 0:
            first = 1
            final_avg_price_change = stock.multiple_price_change.copy()
            final_avg_perc_change = stock.multiple_perc_change.copy()

            # for i in range(len(final_avg_perc_change)):
            #     print("date-range ", i, "  :   ", stock.multiple_perc_change[i], file=f)
            
            continue


        for i in range(len(final_avg_price_change)):
            #add here, divide by length in the next loop
            final_avg_price_change[i] = (final_avg_price_change[i] + stock.multiple_price_change[i])
            final_avg_perc_change[i] = (final_avg_perc_change[i] + stock.multiple_perc_change[i])
            # print("date-range ", i, "  :   ", stock.multiple_perc_change[i], file=f)



    for i in range(len(final_avg_price_change)):

        final_avg_price_change[i] = final_avg_price_change[i] / len(stock_list)  #this finds the average
        final_avg_perc_change[i] = final_avg_perc_change[i] / len(stock_list)


        print("Date range ", i, file=f)
        print("Average Price change for all stocks in this date range: ", final_avg_price_change[i], file=f)
        print("Average Percentage change for all stocks in this date range: ", final_avg_perc_change[i], "%", file=f)


    print("wow", file=f)
    os.system('start excel.exe "../Excel_Sheets/Data.xlsx"')