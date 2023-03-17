
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