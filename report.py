import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
# import matplotlib as plt

win = tk.Tk()
win.title("Seller Marketing Report Generator")
win.resizable(False, False)

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

#################
### Input tab ###
#################

#Labels
dateLbl = ttk.Label(win, text="Date").grid(column=label, row=date)
primeLbl = ttk.Label(win, text="Weekly Prime Seller").grid(column=label, row=prime)
soldSellerLbl = ttk.Label(win, text="Sold Sellers").grid(column=label, row=soldSeller)
soldItemsLbl = ttk.Label(win, text="Sold Items: ").grid(column=label, row=soldItems)
netCartLbl = ttk.Label(win, text="Net Cart").grid(column=label, row=netCart)
ttlQtyLbl = ttk.Label(win, text="Total Qty").grid(column=label, row=ttlQty)
netQtyLbl = ttk.Label(win, text="Net Qty").grid(column=label, row=netQty)
netBPVLbl = ttk.Label(win, text="Net BPV").grid(column=label, row=netBPV)
QCashLbl = ttk.Label(win, text="No. QCash Sellers").grid(column=label, row=QCash)
netQCashSpendingLbl = ttk.Label(win, text="Net QCash Spending").grid(column=label, row=netQCashSpending)

#Entry boxes
primeVar = tk.StringVar()
primeEntry = tk.Entry(win, width=20, textvariable=primeVar).grid(column=entry, row=prime)

soldSellerVar = tk.StringVar()
soldSellerEntry = tk.Entry(win, width=20, textvariable=soldSellerVar).grid(column=entry, row=soldSeller)

soldItemsVar = tk.StringVar()
soldItemsEntry = tk.Entry(win, width=20, textvariable=soldItemsVar).grid(column=entry, row=soldItems)

netCartVar = tk.StringVar()
netCartEntry = tk.Entry(win, width=20, textvariable=netCartVar).grid(column=entry, row=netCart)

ttlQtyVar = tk.StringVar()
ttlQtyEntry = tk.Entry(win, width=20, textvariable=ttlQtyVar).grid(column=entry, row=ttlQty)

netQtyVar = tk.StringVar()
netQtyEntry = tk.Entry(win, width=20, textvariable=netQtyVar).grid(column=entry, row=netQty)

netBPVVar = tk.StringVar()
netBPVEntry = tk.Entry(win, width=20, textvariable=netBPVVar).grid(column=entry, row=netBPV)

QCashVar = tk.StringVar()
QCashEntry = tk.Entry(win, width=20, textvariable=QCashVar).grid(column=entry, row=QCash)

netQCashSpendingVar = tk.StringVar()
netQCashSpendingEntry = tk.Entry(win, width=20, textvariable=netQCashSpendingVar).grid(column=entry, row=netQCashSpending)
#Buttons

#Date Picker

##################
### Report tab ###
##################

#Labels

#Entry boxes

#Buttons

win.mainloop()