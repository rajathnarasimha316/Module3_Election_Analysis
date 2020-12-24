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
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #    print(row)
    headers = next(file_reader)
    print(headers)
    
