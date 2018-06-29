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
    maximum = 0
    maximummonth = 0
    minimum = 0
    minimummonth = 0
    rowints = []
    months = []

    for row in csvreader:
        monthcount = monthcount +1
        netprofitloss += int(row[1])
        if int(row[1]) > maximum:
            maximum = int(row[1])
            maximummonth = str(row[0])
        if int(row[1]) < minimum:
            minimum = int(row[1])
            minimummonth = str(row[0])
        
      
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofitloss))
    print("Average Change: $" + str(round((netprofitloss/monthcount), 2)))

   
   
    
    print("Greatest Increase in Profits: %s ($%s)" %(maximummonth, maximum))

    print("Greatest Decrease in Profits: %s ($%s)" % (minimummonth, minimum))
    
  
   

