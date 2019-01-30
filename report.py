import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import datetime
# import matplotlib.pyplot as plt

win = tk.Tk()
win.title("Seller Marketing Report Generator")
win.geometry('500x500')
win.resizable(False, False)

row=0

while row < 50:
    win.rowconfigure(row, weight=1)
    win.columnconfigure(row, weight=1)
    row += 1

#Column assignments
index = 0 #Reserved for index
label = index + 1
entry = index + 2

#Row assignments
firstRow = 1 #Reserved for header GUI
feature = {'day': 0, 'date': 0, 'prime': 0, 'soldSeller': 0, 'soldItems': 0, 'netCart': 0, 'ttlQty': 0, 'netQty': 0, 'netBPV': 0, 'QCash': 0, 'netQCashSpending': 0}
for index, i in enumerate(feature):
    feature[i] = firstRow + index

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
dayLbl = ttk.Label(input, text="Day").grid(column=label, row=feature['day'])
dateLbl = ttk.Label(input, text="Date").grid(column=label, row=feature['date'])
primeLbl = ttk.Label(input, text="Weekly Prime Seller").grid(column=label, row=feature['prime'])
soldSellerLbl = ttk.Label(input, text="Sold Sellers").grid(column=label, row=feature['soldSeller'])
soldItemsLbl = ttk.Label(input, text="Sold Items: ").grid(column=label, row=feature['soldItems'])
netCartLbl = ttk.Label(input, text="Net Cart").grid(column=label, row=feature['netCart'])
ttlQtyLbl = ttk.Label(input, text="Total Qty").grid(column=label, row=feature['ttlQty'])
netQtyLbl = ttk.Label(input, text="Net Qty").grid(column=label, row=feature['netQty'])
netBPVLbl = ttk.Label(input, text="Net BPV").grid(column=label, row=feature['netBPV'])
QCashLbl = ttk.Label(input, text="No. QCash Sellers").grid(column=label, row=feature['QCash'])
netQCashSpendingLbl = ttk.Label(input, text="Net QCash Spending").grid(column=label, row=feature['netQCashSpending'])

#Entry boxes
dayVar = tk.StringVar()
dayEntry = tk.Entry(input, width=20, textvariable=dayVar)
dayEntry.grid(column=entry, row=feature['day'], columnspan=5)

primeVar = tk.StringVar()
primeEntry = tk.Entry(input, width=20, textvariable=primeVar).grid(column=entry, row=feature['prime'], columnspan=5)

soldSellerVar = tk.StringVar()
soldSellerEntry = tk.Entry(input, width=20, textvariable=soldSellerVar).grid(column=entry, row=feature['soldSeller'], columnspan=5)

soldItemsVar = tk.StringVar()
soldItemsEntry = tk.Entry(input, width=20, textvariable=soldItemsVar).grid(column=entry, row=feature['soldItems'], columnspan=5)

netCartVar = tk.StringVar()
netCartEntry = tk.Entry(input, width=20, textvariable=netCartVar).grid(column=entry, row=feature['netCart'], columnspan=5)

ttlQtyVar = tk.StringVar()
ttlQtyEntry = tk.Entry(input, width=20, textvariable=ttlQtyVar).grid(column=entry, row=feature['ttlQty'], columnspan=5)

netQtyVar = tk.StringVar()
netQtyEntry = tk.Entry(input, width=20, textvariable=netQtyVar).grid(column=entry, row=feature['netQty'], columnspan=5)

netBPVVar = tk.StringVar()
netBPVEntry = tk.Entry(input, width=20, textvariable=netBPVVar).grid(column=entry, row=feature['netBPV'], columnspan=5)

QCashVar = tk.StringVar()
QCashEntry = tk.Entry(input, width=20, textvariable=QCashVar).grid(column=entry, row=feature['QCash'], columnspan=5)

netQCashSpendingVar = tk.StringVar()
netQCashSpendingEntry = tk.Entry(input, width=20, textvariable=netQCashSpendingVar).grid(column=entry, row=feature['netQCashSpending'], columnspan=5)
#Buttons

#Date Picker
today = datetime.datetime.now()

dayVar = tk.StringVar(input)
dayNo = []
for day in range(31):
    dayNo.append(day+1)
dayOption = tk.OptionMenu(input, dayVar, *dayNo).grid(row=feature['date'], column=entry)
dayVar.set(today.day)

monthVar = tk.StringVar(input)
currentMonth = today.strftime("%b")
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthOption = tk.OptionMenu(input, monthVar, *month).grid(row=feature['date'], column=entry+1)
monthVar.set(currentMonth)

yearVar = tk.StringVar(input)
currentYear = today.year
yearNo = []
for year in range(10): #Add +- 10 years to menu
    yearNo.append(currentYear+year+1)
    yearNo.insert(0,currentYear-year)
yearOption = tk.OptionMenu(input, yearVar, *yearNo).grid(row=feature['date'], column=entry+2)
yearVar.set(currentYear)


##################
### Report tab ###
##################

#Labels

#Entry boxes

#Buttons

win.mainloop()