# First import the os module
# This will create file paths across operating systems
import os

# Module for reading CSV files
import csv

import datetime

# Set path for file
csvpath = os.path.join("Resources","budget_data.csv")
## analysis = os.path.join("..", "Analysis", "budget.txt")

#Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile,delimiter =",")
    #dict_reader = csv.DictReader(csvfile)
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvfile)

    # For readability, it can help to assign your values to variables with descriptive names
    months=[]
    profits =[]
    monthly_change =[]
    
    # Read each row of data after the header 
    for row in csv_reader:

        #appending the months and profit in the csvfile to a collections(list)
        months.append(str(row[0]))
        profits.append(int(row[1]))

        #Calculate the total months by len() method. It counts the total rows.
        total_months = len(months)
        
        #Calculates the net total by sum() method
        net_total = sum(profits)

    #print the total months and net total of the budget_data
    print( "Financial Analysis")
    print("--------------------")
    print(f'Total Months: {total_months}')
    print(f"Total :${net_total}")

    #loop through the first row to the last row of profit/losses
    for x in range(1,len(profits)):

        #Calculate monthly change by subtracting the profit of first row to the previous row
        monthly_change_temp = int(profits[x])-int(profits[x-1])

        #append the monthly changes to the monthly_change list
        monthly_change.append(monthly_change_temp)

        #Calculate average change by dividing the total monthly change by the count of rows
        # and the keep only 2 decimal places by rounding method 
        average_change = round(sum(monthly_change)/len(monthly_change),2)

        #Calculate the greatest increase by max() method
        greatest_increase_profit= max(monthly_change)

        #Calculate the greatest decrease by min() method
        greatest_decrease_profit= min(monthly_change)

        #index() method to find the matching month coresponding to the greatest increase in profit. 
        index_greatest_profit = monthly_change.index(greatest_increase_profit)

        #index() method to find the matching month coresponding to the greatest decrease in profit.
        index_decrease_profit = monthly_change.index(greatest_decrease_profit)

    #print the average change,greatest increase in profit and greatest decrease in profit
    print(f"Average Change :${average_change}")
    print(f"Greatest Increase in Profits: {months[index_greatest_profit+1]} (${greatest_increase_profit})")
    print(f"Greatest Decrease in Profits: {months[index_decrease_profit+1]} (${greatest_decrease_profit})")
    
# Specify the file to write to
output_path = os.path.join("Analysis", "report.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    # Write the rows in csv file
    csvwriter.writerow(['Finacial Analysis'])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Total Months:'+ str(total_months)])
    csvwriter.writerow(['Total :$'+ str(net_total)])
    csvwriter.writerow(['Average Change :$' + str(average_change)])
    csvwriter.writerow(['Greatest Increase in Profits: '+ (months[index_greatest_profit+1]) +  '  $('+ str(greatest_increase_profit)+')'])
    csvwriter.writerow(['Greatest Decrease in Profits: '+ (months[index_decrease_profit+1]) +  '  $('+ str(greatest_decrease_profit)+')'])

