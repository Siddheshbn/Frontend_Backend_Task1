from openpyxl import load_workbook
from datetime import datetime
import time
import threading
import math

wb = load_workbook("book3.xlsx")

sheet = wb["Sheet1"]

start = time.time()


def func1():
    threading.Timer(10, func1).start()
    for i in range(0, 8):
        pi_4 = 0.785
        row = (math.sin(i*pi_4), math.cos(i*pi_4))
        sheet.append(row)
        wb.save("book3.xlsx")
        wb.close()
        print('func1 is running')


func1()

# wb.save("book3.xlsx")

## PRINTING THE TIME
# time_sec_str = datetime. now(). strftime("%S")
#
# time_sec_int = int(time_sec_str)
#
# print(type(time_sec_int))

## RUN A FUNCTION AFTER A FIXED INTERVAL OF TIME
# def printit():
#   threading.Timer(0.3, printit).start()
#   print ("Hello, World!")
#
# printit()
