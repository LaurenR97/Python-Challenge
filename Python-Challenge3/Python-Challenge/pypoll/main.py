import os
import csv

# Define the path to the CSV file containing poll data

election_csv = os.path.join("/Users/lauren-ashleyrutland/Desktop/Python-Challenge3/Python-Challenge/pypoll/resources/election_data.csv")

# Initialize the variables
total_votes = 0
candidate_votes = {}
winner = ""
winner_votes = 0

# Open the CSV file
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first
    csv_header = next(csvreader)
        
    # Iterate over the csv reader object
    for data in csvreader:

       
        total_votes += 1
        
        # Extract the candidate name
        candidate_name = data[2]
        
        # Update the vote count for the candidate
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Print the election results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open("/Users/lauren-ashleyrutland/Desktop/Python-Challenge3/Python-Challenge/pypoll/analysis/election_analysis.csv", "w", newline="") as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=",")
    
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        csvwriter.writerow([f"{candidate}: {percentage:.3f}% ({votes})"])
    csvwriter.writerow([f"Winner: {winner}"])




