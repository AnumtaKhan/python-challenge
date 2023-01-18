# Import dependencies
import os
import csv

# Select the File Path
csv_PyPoll = os.path.join("Resources", "election_data.csv")

# Lists to store data
Ballot_ID = []
Candidate = []
Count = 0
Each_Candidate = []
Count_Of_Votes = []
Percentage_Of_Votes = []

# Open so csv can be read
with open(csv_PyPoll) as csvfile:
    csvreader = csv.reader(csvfile)
    # Make sure the data is read after the header
    csv_header = next(csvreader)

    # Read through each row (after header)
    for row in csvreader:
        Ballot_ID.append(int(row[0]))
        Candidate.append(row[2])

        # Count of vote
        Count = Count + 1

    # Using a for loop, compute the list of candidates, total number of votes, and percentage of votes for each candidate
    for i in set(Candidate):
        Each_Candidate.append(i)

        x = Candidate.count(i)
        Count_Of_Votes.append(x)

        y = (x/Count)*100
        Percentage_Of_Votes.append(y)

    # Compute the Highest Number of Votes received
    Highest_Votes = max(Count_Of_Votes)
    

    # Print the analysis to the terminal
    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {len(Ballot_ID)}")
    print("------------------------------")
    for j in range(len(Each_Candidate)):
        print(f"{Each_Candidate[j]}: {round(Percentage_Of_Votes[j],3)}% ({Count_Of_Votes[j]})")
    print("------------------------------")
    print(f"Winner: {Each_Candidate[Count_Of_Votes.index(Highest_Votes)]}")
    print("------------------------------")
    
# Export a text file with results using csvwriter
output = os.path.join("Analysis", "PyPoll_Analysis.txt")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Total Votes: {len(Ballot_ID)}"])
    csvwriter.writerow(["----------------------------------"])
    for j in range(len(Each_Candidate)):
        csvwriter.writerow([f"{Each_Candidate[j]}: {round(Percentage_Of_Votes[j],3)}% ({Count_Of_Votes[j]})"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([f"Winner: {Each_Candidate[Count_Of_Votes.index(Highest_Votes)]}"])