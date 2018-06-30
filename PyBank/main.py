import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('budget_data.csv')

with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

   

    monthcount = 0
    netprofitloss = 0

    profitorloss = 1154293
    listprofitloss = []
    
  
    maximum = 0
    maximummonth = 0
    minimum = 0
    minimummonth = 0
  

    for row in csvreader:
        monthcount = monthcount +1
        netprofitloss += int(row[1])

        profitloss = int(row[1]) - profitorloss
        listprofitloss.append(profitloss)
        profitorloss = int(row[1])



        if int(row[1]) > maximum:
            maximum = int(row[1])
            maximummonth = str(row[0])
        if int(row[1]) < minimum:
            minimum = int(row[1])
            minimummonth = str(row[0])
    averagechange = sum(listprofitloss)/(len(listprofitloss)-1)

    print("Financial Analysis")
    print("----------------------------")  
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofitloss))
   
   
    print("Average Change: $" + str(round((averagechange), 2)))

   
   
    
    print("Greatest Increase in Profits: %s ($%s)" %(maximummonth, maximum))

    print("Greatest Decrease in Profits: %s ($%s)" % (minimummonth, minimum))
text_file = open("Output.txt", "w")
text_file.write("Financial Analysis" +"\n" +
                "----------------------------" +"\n" +
                "Total Months: " + str(monthcount) + "\n" + 
                "Total: $" + str(netprofitloss) + "\n" +
                "Average Change: $" + str(round((averagechange), 2)) + "\n" +
                "Greatest Increase in Profits: %s ($%s)" %(maximummonth, maximum) + "\n" +
                "Greatest Decrease in Profits: %s ($%s)" % (minimummonth, minimum) + "\n")

   
  
   



   
   
    
    