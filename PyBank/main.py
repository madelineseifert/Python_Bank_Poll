import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('budget_data.csv')

with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    monthcount = 0
    netprofitloss = 0
    increase = 0
    decrease = 0

    for row in csvreader:
        monthcount = monthcount +1
        netprofitloss += int(row[1])
        #increase = max(float(row[1])
        
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofitloss))
    print("Average Change: $" + str(round((netprofitloss/monthcount), 2)))
    print(str(increase))
    print(row)

    
  
    

