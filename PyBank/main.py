# Import dependencies
import os
import csv

# Select the File Path
csv_PyBank = os.path.join("Resources", "budget_data.csv")

# Lists to store data
Date = []
Profit_Losses = []

# Open so csv can be read
with open(csv_PyBank) as csvfile:
    csvreader = csv.reader(csvfile)
    # Make sure the data is read after the header
    csv_header = next(csvreader)

    # Read through each row (after header)
    for row in csvreader:
        Date.append(row[0])
        Profit_Losses.append(int(row[1]))

    # Lists to store data
    Changes = []
    Max_Month = []
    Min_Month = []
    Changes_Max_Month = []
    Changes_Min_Month = []

    # Using a for loop, compute the net total amount of Profit/Losses over the entire period
    for i in range(1,len(Profit_Losses)):
        Changes.append(Profit_Losses[i]-Profit_Losses[i-1])
        Changes_Max_Month.append(Date[i])
        Changes_Min_Month.append(Date[i])

    # Compute the change in Profit/Losses and the average of those changes
    Mean_Changes = sum(Changes) / len(Changes)
    Max_Changes = max(Changes)
    Min_Changes = min(Changes)

    # Using a for loop, Compute the greatest increase and decrease in profits (date and amount) over the entire period
    for i in range(1,len(Changes)):
        if Changes[i] == Max_Changes:
            Max_Month = Changes_Max_Month[i]
        if Changes[i] == Min_Changes:
            Min_Month = Changes_Min_Month[i]
        

    # Print the analysis to the terminal
    print("Financial Analysis")
    print("------------------------------------------------")
    print(f"Total Months: {len(Date)}")
    print(f"Total: ${sum(Profit_Losses)} ")
    print(f"Average Change: ${round(Mean_Changes,2)}")
    print(f"Greatest Increase in Profits: {Max_Month} (${Max_Changes})")
    print(f"Greatest Decrease in Profits: {Min_Month} (${Min_Changes})")

# Export a text file with results using csvwriter
output = os.path.join("Analysis", "PyBank_Analysis.txt")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Total Months: {len(Date)}"])
    csvwriter.writerow([f"Total: ${sum(Profit_Losses)}"])
    csvwriter.writerow([f"Average Change: ${round(Mean_Changes,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {Max_Month} (${Max_Changes})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {Min_Month} (${Min_Changes})"])