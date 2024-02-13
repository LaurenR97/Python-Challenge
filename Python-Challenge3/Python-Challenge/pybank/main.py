import csv
import os

# Define the path to the CSV file
bank_cvs = os.path.join ("/Users/lauren-ashleyrutland/Desktop/Python-Challenge3/Python-Challenge/pybank/resources/budget_data.csv")

# Initialize variables 

total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read CSV file
with open(bank_cvs, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    next(csvreader)
    
    # Iterate through each row 
    for row in csvreader:
        # Update total months
        total_months += 1
        
        # Retrieve date and profit/loss 
        date = row[0] 
        profit_loss = int(row[1])
        
        # Update total profit/loss
        total_profit_losses += profit_loss
        
        # Calculate change in profit/loss from previous month
        change = profit_loss - previous_profit_loss
        
        # Update previous profit/loss for next iteration
        previous_profit_loss = profit_loss
        
        # Update greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase = [date, change]
        
        # Update greatest decrease in losses
        if change < greatest_decrease[1]:
            greatest_decrease = [date, change]
        
# Calculate average change
average_change = round(total_profit_losses / total_months, 2)

# Print the financial analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})")

#write to csv

with open ("/Users/lauren-ashleyrutland/Desktop/Python-Challenge3/Python-Challenge/pybank/analysis/budget_analysis.csv",'w',newline="") as csvfile:


    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${total_profit_losses}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})"])
    csvwriter.writerow([f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})"])



