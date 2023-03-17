import sys

def Collect_User_Input():

    workbook_name = input("What is the name of the Excel file you would like to save data to? (withought the .xlsx):   ")
    workbook_path = f"../Excel_Sheets/{workbook_name}.xlsx"

    print(  """\n\nEnter the ranges of buy and sell dates that you want to compute.
        The number you input is the number of days BEFORE the stock's Ex-dividend date.
        You can do negative numbers to act as days after the Ex-dividend date\n
        EXAMPLE:
        
        Beginning of Buy Date range: 21
        End of Buy Date range: 7
        Beginning of Sell Date range: 3
        End of Sell Date range: -3

        If you want to calculate the averages for all possibilities between buying 21 days before up to 7 days before
        and for selling 3 days before to 3 days after, you would input the values above.
        Now input your wanted values\n\n
        """)
    

    beginning_buy_range = int(input("Beginning of Buy Date range: "))
    end_buy_range = int(input("End of Buy Date range: "))
    beginning_sell_range = int(input("Beginning of Sell Date range: "))
    end_sell_range = int(input("End of Sell Date range: "))

    # Do logic checks now to make sure date ranges work

    # Just switch dates if the beginning/end date is further in the past than the beginning
    if end_buy_range > beginning_buy_range:
        end_buy_range, beginning_buy_range = beginning_buy_range, end_buy_range

    if end_sell_range > beginning_sell_range:
        end_sell_range, beginning_sell_range = beginning_sell_range, end_buy_range

    # Check if we are selling before we buy
    if beginning_sell_range >= end_buy_range:
        print("ERROR: Trying to sell before buying")
        print("Exiting Script")
        sys.exit()


    return (workbook_path,
            beginning_buy_range,
            end_buy_range,
            beginning_sell_range,
            end_sell_range)






























# TODO Started creating this and realized that I want to do it different in the long run so I am not going to finish it, but just keep it here as a reminder
def Create_Excel_Tables(stock, ws, beg_buy_range, end_buy_range, beg_sell_range, end_sell_range):
    """
    Creates the tables in Excel

    Parameters:
    stock: A stock object
    ws: An excel WorkSheet
    beg_buy_range: (int) 
    end_buy_range: (int) 
    beg_sell_range: (int) 
    end_sell_range: (int) 

    Returns:
    Nothing
    """
    
    
    
    
    # create row titles
    row_titles = []
    for num in range(end_buy_range, beg_buy_range):
        row_titles.append(str(num))

    # Create Column titles
    col_titles = []
    for num in range(end_sell_range, beg_sell_range):
        col_titles.append(str(num))