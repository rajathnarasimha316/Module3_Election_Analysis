import datetime
import csv
import os
import subprocess

'''
Open the data file.
Write down the names of all the candidates.
Add a vote count for each candidate.
Get the total votes for each candidate.
Get the total votes cast for the election
'''
with open("election_results.csv", "r") as election_data:
    # Print the file object.
    ED = election_data.read()
    # print(ED)
    election_data.close()

# Create a filename variable to a direct or indirect path to the file.

# Using the with statement open the file as a text file.
with open("election_analysis.txt", "w") as txt_file:
    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in Election\n")
    txt_file.write("--------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

total_votes = 0
candidate_options =[]
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    for row in file_reader:
        total_votes +=1
        # print(total_votes)
        candidate_name = row[2]
        # print(candidate_name)
        # candidate_options.append(candidate_name)
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
           # Begin tracking that candidate's vote count. 
        candidate_votes[candidate_name] += 1
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # vote_percentage = format(v_p, '.1f')
        #vote_percentage1 = int(vote_percentage)
        # Print the candidate name and percentage of votes.
        print("\n")
        print(f"{candidate}: received {vote_percentage}% of the vote.")
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate
         print(f"The winning Candidate is", winning_candidate)
         print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
         winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
  
    



    
