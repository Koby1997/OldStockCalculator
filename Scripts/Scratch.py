import yfinance as yf
import pandas as pd
import time
import datetime
import openpyxl
from openpyxl import load_workbook
import os
import time
import psutil

pd.set_option('display.max_rows', None)

workbook_name = input("What workbook would you like to save to?\n")
workbook_path = f"../Excel_Sheets/{workbook_name}.xlsx"

for process in psutil.process_iter():
    print(process)
    if process.name() == 'EXCEL.EXE':
        # Get the full path of the Excel process
        print("Do I get here?")
        process_path = process.exe()
        print("Process path:   ", process_path)
        # Check if the path of the open workbook matches the path we want to check


        print("FIRST:   ", os.path.normcase(workbook_path))
        print("SECOND:   ", os.path.normcase(process_path.split(' /')[0]))
        if os.path.normcase(workbook_path) == os.path.normcase(process_path.split(' /')[0]):
            # Close the workbook
            process.terminate()
            print(f"The workbook {workbook_path} was already open and has been closed.")


try:
    workbook = load_workbook(workbook_path)

except FileNotFoundError:
    print("That workbook doesn't exist. Creating workbook")
    workbook = openpyxl.Workbook()
    workbook.save(workbook_path)

except Exception as e:
    print("The workbook is already open. Closing the Workbook first")


time.sleep(2)




os.system(f'start excel.exe {workbook_path}')