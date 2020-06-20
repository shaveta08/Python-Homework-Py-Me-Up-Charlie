import os
import csv

#function to draw the line in output.
def drawline():
    for _ in range(30):
        print("-",end="")
    print("")

#opening and reading the file
csvpath = os.path.join('Resources','budget_data.csv')
opened_file = open(csvpath,encoding='utf8')
read_file = csv.reader(opened_file)

#Converting the data in list of list.
budget_data = list(read_file)

# Counting the total number of excluding the header from the list
total_months = len(budget_data[1:])

#list to store the profit and loss value converted to int with month name.
profit_loss = []

#total value in profit/loss
total_amount = 0

for row in budget_data[1:]:
    profit_loss.append([row[0],int(row[1])])   
    total_amount =  total_amount + int(row[1])

#calculating the greatest increase and decrease in profit and loss.
#dictionary : profit_loss_change. 
#Key: month-year Values:Difference in the profit/loss from the previous year.
profit_loss_change = {}
max_profit = 0
min_profit = 0

for i in range(len(profit_loss) - 1):
   profit_loss_change[profit_loss[i+1][0]] = int(profit_loss[i+1][1] - profit_loss[i][1])

#Calculating the max and min values of profit changes from dictionary
#Also finding out the respective months.
max_month = max(profit_loss_change, key=profit_loss_change.get)
max_profit = profit_loss_change[max(profit_loss_change, key=profit_loss_change.get)]
min_month = min(profit_loss_change, key=profit_loss_change.get)
min_profit = profit_loss_change[min(profit_loss_change, key=profit_loss_change.get)]

# average change in profits/loss over the period of time.
# average change = ((final profit/loss) - (initial profit/loss)) / total number of months in between.
average_change = round((int(budget_data[len(budget_data)-1][1]) -  int(budget_data[1][1]))/ (total_months - 1),2)

# Printing the results on the screen and Also writing them down in text file.
text_file_path = os.path.join('Analysis','Result.txt')
text_file = open(text_file_path,'w')

print("Financial Analysis")
text_file.write("Financial Analysis\n")

drawline()
text_file.write("------------------------------\n")

print(f"Total Months: {total_months}")
text_file.write(f"Total Months: {total_months}\n")

print(f"Total: {total_amount}")
text_file.write(f"Total: {total_amount}\n")

print(f"Average Change: ${average_change}")
text_file.write(f"Average Change: ${average_change}\n")

print(f"Greatest Increase in Profits: {max_month} (${max_profit})")
text_file.write(f"Greatest Increase in Profits: {max_month} (${max_profit})\n")

print(f"Greatest Decrease in Profits: {min_month} (${min_profit})")
text_file.write(f"Greatest Decrease in Profits: {min_month} (${min_profit})\n")

text_file.close()
