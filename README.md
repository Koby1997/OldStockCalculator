
# StockCalculator

Creating scripts to simulate a stock strategy over historical data to see if it is a viable strategy for real trading. Also to help learn Python.

  

I have a simple stock trading strategy that I cannot see the fallacy in. It is simply buying a stock a little before the stock pays the dividend, then selling, even before they pay the dividend out. When you try to research this strategy, everyone talks about trying to hold the stock and earn on the actual dividend, but that is not what I want to do. I belive I have noticed a trend where the stock will rise, but then after the payout the stock falls. This is known and makes sense. The amount the stock falls is related to the payout of the stock. I want to see if I can capitalize on the rise right before the fall. These scripts are just to see if there is in fact a rise right before the dividend payout an overwhelming majority of the time.

  &nbsp;
  &nbsp;

## LUCAS NOTES:
&nbsp;
  ## How the code is organized/How it works:


### QuickFind.py

The QuickFind.py is really just my like quick script to try something or learn something from python. Right now, it is a quick script to see if

 **1. A stock actually has data for ex_dividend dates
 2. It prints how many that stock has**
  

In the main script I put a check to make sure that we get at least 50 data points in order to add it to the overall calculations. So if a stock doesn't even have 50 dates, I don't waste time adding it because it will be deleted anyways.

Also, a stock can have more than 50 dates, but that doesn't mean it has data for each of those dates, so a stock can still be kicked out. So I use this quick script to see if I think it will have plenty of dates for the main script. You can put one in that is just over 50, but ctrl-F the output to see if it actually went all the way through.

So to use the QuickFind.py, all you really need to do is just change the "all_tickers" list at the top to include any stock symbols you want.

  &nbsp;
  &nbsp;

### UpdatedExdividendDates.py

Ok so the most up to date script is UpdatedExdividendDates.py 
That is the script I am trying to get data from currently.
The UpdatedExdividendDates.py script will write an output.txt file(or overwrite the file. I delete it just in case though haha). In that file will be 2 sections:

  

 **1. The average for a stock for each date range
 2. The average for the date range as a whole with all stocks included**


  

Once you have that output.txt file, I like to open it in VSCode and use the find feature on it. I also like to copy it to a temporary file so I can delete stuff and mess with it without worrying about losing the data.

Do Ctrl-f and choose the .* option to put in a regex statement. Then put this:

  

\d+\.\d+\s?%

  

This should show any percentages. Then you can push ctrl-shift-L to highlight those percentages and copy them. Remember that this will take the percentages of both of the sections, so you should really delete the section you don't care about first.

If you want to pull out other data with regex, just ask ChatGTP haha give it a couple sections of the output file and literally ask how to get it with regex in vscode find feature.



Things I want to figure out to save a ton of time:

 - Once I get just the percentages, I can put them in a column in Excel, but I don't know how to easily get them in a grid to match to buy_day/sell_day. I have tried to google, to use ChatGTP, I still can't find a good way other than manually putting them into a grid which takes forever. Especially if we are going to run this at different times with different stocks and manually average them afterwards. 

&nbsp;
&nbsp;

### StockClass.py

There is a StockClass.py that organizes how we can keep track of individual stocks. Each stock object will have:

 - a symbol -> "AAPL"


*Temporary Lists:*
 - **single_price_change list** -> this is a list (think array for other languages) where each "box" is the average for a single date range. So when this list is full, it has the averages for each date range for one stock.
 - **single_perc_change list** -> same as above but for percentages
 
 *Temporary properties:*
 - **single_avg_price_change** -> the average price change for a SINGLE date range, for all historical ex-dividend days
 - **single_avg_perc_change** -> the average percent change for a SINGLE date range, for all historical ex-dividend days


*Main Lists:*

 - **multiple_price_change list**  -> holds an average price change for each date range for one stock
 - **multiple_perc_change list**  -> same as above but for percentages



So basically it flows down.

 1. Save ONE comparison from ONE date range into single_change list
 2. When all comparisons are done, that list will be full
 3. Find the average for that date range
 4. Put that average into single_avg_change variable
 5. Append single_avg_change to the multiple_change list

The final lists will be in the order of the for loops in the code. Meaning if you are doing buy days from 10-12 days before, and sell days 1-3 days before, your array will be like this:
multiple_change_list =  [10,1]  [10,2]  [10,3]  [11,1]  [11,2] . . . . . . . .
If that doesn't make sense, I can explain more over the phone. 

The class also has methods to calculate the averages. It is simple math
The main method though is the one that "cleans" the single properties/lists. It basically calls the average methods and then resets the values of those properties/lists so they can be reused for the next date range


&nbsp;
&nbsp;

## Code Flow:

The top is just the list of stocks we want to check.
We do a quick for loop to actually create the Stock objects for each stock symbol we gave it.
We then have a quadruple for loop. Not efficient, but I dunno how else to do this more efficiently haha this is why the code is so slow. But we are also going through a ton of data.

>1. **Loop through each stock**
	  Find all the ex-dividend dates for this stock and save them in a list
	  Convert the data to the type we can use
	 
>>>2. **Loop through each buy day**
	
>>>>>3. **Loop through each sell day**
			Keep track of data points, we want at least 50 in each date range
			
>>>>>>>4. **Loop through each ex_dividend date that the stock has**
			This is where the comparisons happen
			We get the data from the buy/sell dates and find the difference price wise and percentage wise and append that information to the correct list for that stock.
			
>>>>>_3. **Back in the Sell day loop**
			 Print the info for that date range
			 "Clean" the single properties to restart for the next date range with a new Sell day
			 
>>>_2. **Back in the Sell day loop**
	 Just checking if there was enough data points

>_1. **Finished current stock**
This stock object now has all the information we want
Print information to the terminal just to help know the progress of the script

After the loops are done, we can now calculate our total averages across all stocks.
We do a double for loop now
Before the loops, we create out FINAL empty lists
The first loop then iterates over the stock objects again.
The second loop iterates over the current stock's multiple_change list and takes the value at index [i] and adds it to index [i] of our FINAL list, then divide by 2 to get the average. 
once this goes through all the stocks, we now have a list of the average change over all stocks for a certain date range.
Lastly we iterate over that list to print out the final results





Scratch notes:
need to do: pip install openpyxl
in order to write to excel files