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

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

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

        # 3: Extract the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add the candidates name to the candidate list
            candidate_options.append(candidate_name)

            # Give candidates vote & candidate name a value 0
            candidate_vote[candidate_name] = 0
            
        # Add a vote to that candidates count
        candidate_vote[candidate_name] += 1

        # 4a: Write an if statement that checks that the county does not match 
        #any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties
            county_options.append(county_name)

            #4c: Begin tracking the county's vote count
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count
        county_votes[county_name] += 1

# Save to a txt file
with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Resluts\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Initialize a variable to hold the county's votes as they are retrieved from the county votes dictionary
        total_county_votes = county_votes[county_name]

        # 6c: Calculate the percentage of votes for the county.
        percentage_votes_county = float(total_county_votes) / float(total_votes) * 100

        county_results = (f"{county_name}: {percentage_votes_county:.1f}% ({total_county_votes:})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (total_county_votes > winning_county_count) and (percentage_votes_county > winning_county_percentage):
            #winning_county_count = total_county_votes
            winning_county_count = total_county_votes
            victorious_county = county_name

    # 7: Print the county with the largest turnout to the terminal
    largest_county = (
        f"-------------------------\n"
        f"Largest County: {victorious_county}\n"
        f"-------------------------\n")
    print(largest_county)
    # 8: Save the county with the largest turnout to a text file 
    txt_file.write(largest_county)
    # Determine the percentage of votes for each candidate by looping through the counts

    # Iterate (loop) through the candidate list
    for candidate_name in candidate_vote:

        # Retrieve vote count of a candidate 
        votes = candidate_vote[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate

    # To Do: print out each candidate's name, vote count, and percentage of votes to the terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Create variable for candidate_results that will print to txt file
        candidate_results = (f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        # save the candidates results to our text file
        txt_file.write(candidate_results)

        # Determing if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent -
            
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

        # Print the candidate name and percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        
    # To Do: print out the winning candidate, vote count and percentage to terminal
    winning_candidate_summary = (f"---------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------\n")

    # Save the winning candidate's name to the texr file
    txt_file.write(winning_candidate_summary)

    print(winning_candidate_summary)

    # Print the candidates vote dictionary
    #print(candidate_vote)
    




    

