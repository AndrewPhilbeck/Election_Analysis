# Import (add) our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a varable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Assign a variable for total votes = 0
total_votes = 0

# Declare a new list, the candidates 
candidate_options = []

# Declare a candidate vote dictionary {}
candidate_vote = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do:read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidates name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add the candidates name to the candidate list
            candidate_options.append(candidate_name)

            # Give candidates vote & candidate name a value 0
            candidate_vote[candidate_name] = 0
            
        # Add a vote to that candidates count
        candidate_vote[candidate_name] += 1


# Determine the percentage of votes for each candidate by looping through the counts

# Iterate (loop) through the candidate list
for candidate_name in candidate_vote:

    # Retrieve vote count of a candidate 
    votes = candidate_vote[candidate_name]

    # Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # Determine winning vote count and candidate

# To Do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # 1 Determing if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2 If true then set winning_count = votes and winning_percent -
        
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # 3 Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

    # Print the candidate name and percentage of votes
#print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
    
# To Do: print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (f"---------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"---------------------\n")

print(winning_candidate_summary)

# Print the candidates vote dictionary
#print(candidate_vote)
    




    

# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote