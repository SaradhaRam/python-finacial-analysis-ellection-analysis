# First import the os module
# This will create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# declare the empty variables globally to access them any where we want in this script
total_votes = 0
candidates = []
candidate_dict = {}

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvfile)

    # For readability, it can help to assign your values to variables with descriptive names
    votes = []

    # Read each row of data after the header
    for row in csv_reader:
        # appending the votes and candidates to a list
        votes.append(int(row[0]))
        candidates.append(row[2])

    # Calculate the total votes by len() method. It counts the total rows.
    total_votes = len(votes)

    # print the total votes
    print("Election Result")
    print("-----------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "report.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize the csv.writer
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Total Votes:' + str(total_votes)])
    csvwriter.writerow(['-----------------'])

    # To remove duplicates we can use set () method
    unique_set = set(candidates)

    # run the loop for each unique candidates
    for candidate in unique_set:

        # Count the total votes for individual candidates using count() method.
        votes_per_candidate = candidates.count(candidate)

        # create a dictionary by keeping candidate as a key and value as a votes per candidate
        candidate_dict[candidate] = votes_per_candidate

    # Create a empty dictionary and store the sorted keys into it.
    sorted_dict = {}
    sorted_keys = sorted(candidate_dict, key=candidate_dict.get, reverse=True)

    # Iterating for assigning the sorted values(candidate_dict) to the correct keys(candidate)
    for candidate in sorted_keys:
        sorted_dict[candidate] = candidate_dict[candidate]

    #Iterating the  sorted candidate dictionary for printing the required values
    for candidate, votes_per_candidate in sorted_dict.items():

     # Calculate the percentage for each candidate by dividing the votes per candidate
        # and total votes then multiply by 100. Do round() method for 3 decimal places.
        percentage_per_candidate = round(((votes_per_candidate/total_votes) * 100), 3)

    # print the candidate name and percentage and votescount for each candidate
        print(f"{candidate}: {percentage_per_candidate}%  ({votes_per_candidate})")
        csvwriter.writerow(
            [str(candidate) + " : " + str(percentage_per_candidate)+'% ' + str(votes_per_candidate)])

    # print the results in the terminal
    print("----------------")
    winner = next(iter(sorted_dict))
    print(f"Winner : {winner}")
    print("----------------")

    # Write the rows in csv file
    csvwriter.writerow(['-----------------'])
    csvwriter.writerow(['Winner: ' + str(winner)])
    csvwriter.writerow(['-----------------'])
