# Election_Analysis

## Project Overview
A Colorado Board requested an election audit for a recent local congressional election. This audit will reveal the number of votes, along with the different counties involved and the the number of votes from those counties. Finally, the audit will reveal the candidates, how many votes each received and who the winning candidate was.

### The Goals:
1. Calculate the total number of votes cast in the election.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.12, Visual Studio Code, 1.73.0

## Summary
The analysis of the election show that:
- There were 369,711 tota votes cast from three counties:
    -  Jefferson county accounted for 10.5% of the vote (38,855 total)
    -  Denver county accounted for 82.8% of the vote (306,055 total; Largest)
    -  Arapahoe county accounted for 6.7% of the vote (24,801 total)
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote with 85,213 total votes. 
    - Diana DeGette received 73.8% of the vote with 272,892 total votes.
    - Raymon Anthony Doane received 3.1% of the vote with 11,606 total votes. 
 - The winner of the election was:
    - Candidate Diana DeGette who received 73.8% of the vote and 272,892 total votes.
    
## Election Audit Summary
This program could be used for further election audits simply by imorting differnet CSV files as elections were held, so long as the same information type is in the same row as the current file. With more information the code could be changed to gather data based on when a person voted, showing the statistics for early voting as well as mail in ballots. This is as simple as adding another row of information to the CSV file and adding another loop of code to pull out the date and type of vote cast (early/mail in). 
    
 ## Challenge Overview
 
Beginning with only the goal of completing the election audit and the csv vile containing all the election information the challenge was to create a program which would produce the desired results. This was done by utalizing Python within Visual Studio Code. This allowed me to import the CSV file into the Visual Studio and complete the process of compiling the desired data: total votes cast, total number of candidates in election, total percentage of votes and number of votes each candidate received as well as a the winning candidate, vote count and percentage.

## Challenge Summary

The challenge was accomplished by importing the CSV file in to VS Code, assigning variables which applied to each peice of information I was required to find (ex. total votes & candidate names). Once all variables were assigned I used a _with_ statement to skip the headers (top row) of data and look through the _Ballot ID_, _County_, and _Candidate_ name. With a _for_ loop I was able to determine there were only three candidates in the race and see how many votes each candidate received. This information was saved to a text file for easy access. Once total number of votes and votes each candidate received were found I was able to display this information as a percentage. Once this was done the informaiton for the winning candidate was compiled and all relevant information was saved to the text file (election_analysis.txt).
