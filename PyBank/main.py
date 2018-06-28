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
    rowints = []
    months = []

    for row in csvreader:
        monthcount = monthcount +1
        netprofitloss += int(row[1])
        rowint = int(row[1])
        rowints.append(rowint)
        months.append(row[0])
        
      
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofitloss))
    print("Average Change: $" + str(round((netprofitloss/monthcount), 2)))

    profitlist = zip(months, rowints)
    listlength = len(profitlist)
    for i in range(listlength):
        maximum = max(profitlist)
        print("Greatest Increase in Profits: %s ($%r)" % (maximum))

        minimum = min(profitlist)
        print("Greatest Decrease in Profits: %s ($%r)" % (minimum))
    
  
   

