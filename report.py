import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
# import matplotlib as plt

win = tk.Tk()
win.title("Seller Marketing Report Generator")
win.geometry('500x500')
win.resizable(False, False)

row=0

while row < 50:
    win.rowconfigure(row, weight=1)
    win.columnconfigure(row, weight=1)
    row+=1

#Column assignments
index = 0 #Reserved for index
label = index + 1
entry = index + 2

#Row assignments
header = 0 #Reserved for header GUI
date = header + 2
prime = header + 3
soldSeller = header + 4
soldItems = header + 5
netCart = header + 6
ttlQty = header + 7
netQty = header + 8
netBPV = header + 9
QCash = header + 10
netQCashSpending = header + 11

################
### Notebook ###
################

nb = ttk.Notebook(win) #Instantiate Notebook widget and place it in main window
nb.grid(row=1, column=0, rowspan=49, columnspan=50, sticky='NSEW')

#Input tab
input = ttk.Frame(nb) #Instantiate Frame (tab) widget and attach it to Notebook widget
nb.add(input, text="Input")

#Report tab
report = ttk.Frame(nb)
nb.add(report, text="Report")

#################
### Input tab ###
#################

#Labels
dateLbl = ttk.Label(input, text="Date").grid(column=label, row=date)
primeLbl = ttk.Label(input, text="Weekly Prime Seller").grid(column=label, row=prime)
soldSellerLbl = ttk.Label(input, text="Sold Sellers").grid(column=label, row=soldSeller)
soldItemsLbl = ttk.Label(input, text="Sold Items: ").grid(column=label, row=soldItems)
netCartLbl = ttk.Label(input, text="Net Cart").grid(column=label, row=netCart)
ttlQtyLbl = ttk.Label(input, text="Total Qty").grid(column=label, row=ttlQty)
netQtyLbl = ttk.Label(input, text="Net Qty").grid(column=label, row=netQty)
netBPVLbl = ttk.Label(input, text="Net BPV").grid(column=label, row=netBPV)
QCashLbl = ttk.Label(input, text="No. QCash Sellers").grid(column=label, row=QCash)
netQCashSpendingLbl = ttk.Label(input, text="Net QCash Spending").grid(column=label, row=netQCashSpending)

#Entry boxes
primeVar = tk.StringVar()
primeEntry = tk.Entry(input, width=20, textvariable=primeVar).grid(column=entry, row=prime)

soldSellerVar = tk.StringVar()
soldSellerEntry = tk.Entry(input, width=20, textvariable=soldSellerVar).grid(column=entry, row=soldSeller)

soldItemsVar = tk.StringVar()
soldItemsEntry = tk.Entry(input, width=20, textvariable=soldItemsVar).grid(column=entry, row=soldItems)

netCartVar = tk.StringVar()
netCartEntry = tk.Entry(input, width=20, textvariable=netCartVar).grid(column=entry, row=netCart)

ttlQtyVar = tk.StringVar()
ttlQtyEntry = tk.Entry(input, width=20, textvariable=ttlQtyVar).grid(column=entry, row=ttlQty)

netQtyVar = tk.StringVar()
netQtyEntry = tk.Entry(input, width=20, textvariable=netQtyVar).grid(column=entry, row=netQty)

netBPVVar = tk.StringVar()
netBPVEntry = tk.Entry(input, width=20, textvariable=netBPVVar).grid(column=entry, row=netBPV)

QCashVar = tk.StringVar()
QCashEntry = tk.Entry(input, width=20, textvariable=QCashVar).grid(column=entry, row=QCash)

netQCashSpendingVar = tk.StringVar()
netQCashSpendingEntry = tk.Entry(input, width=20, textvariable=netQCashSpendingVar).grid(column=entry, row=netQCashSpending)
#Buttons

#Date Picker
dayVar = tk.StringVar(input)
dayNo = []
for day in range(31):
    dayNo.append(day+1)
dayOption = tk.OptionMenu(input, dayVar, *dayNo).grid(row=date, column=entry)

monthVar = tk.StringVar(input)
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthOption = tk.OptionMenu(input, monthVar, *month).grid(row=date, column=entry+1)

yearVar = tk.StringVar(input)
currentYear = 2019
yearNo = []
for year in range(10): #Add +- 10 years to menu
    yearNo.append(currentYear+year+1)
    yearNo.insert(0,currentYear-year)
yearOption = tk.OptionMenu(input, yearVar, *yearNo).grid(row=date, column=entry+2)


##################
### Report tab ###
##################

#Labels

#Entry boxes

#Buttons

win.mainloop()