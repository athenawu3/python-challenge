import os
import csv

# path to CSV file
file_path = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# read CSV file
with open (file_path, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    data = list(csv_reader)

    # print
    print(" ")
    print("Election Results")
    print("-------------------------")

    ## initialize lists and variables
    vote_count = 0
    candidate_list = []
    prev_candidates = []
    percentage_list = []

    # total number of votes
    for row in data:
        vote_count = vote_count + 1
    print(f"Total Votes: {vote_count}")
    print("-------------------------")

    # candidate list
    for row in data:

        candidate = row[2]
        if candidate not in prev_candidates:
            candidate_list.append(candidate)
            prev_candidates.append(candidate)

    # number and % of votes per candidate
    length = len(candidate_list)
    for i in range(length):
        candidate_count = 0
        for row in data:
            if row[2] == candidate_list[i]:
                candidate_count = candidate_count + 1
        candidate_percentage = candidate_count / vote_count
        percentage = "{:.3%}".format(candidate_percentage)
        print(f"{candidate_list[i]}: {percentage} ({candidate_count})")
        percentage_list.append(candidate_percentage)

    # winner of election based on popular vote
    winner_percentage = max(percentage_list)
    winner_index = percentage_list.index(winner_percentage)
    winner_candidate = candidate_list[winner_index]

    #print
    print("-------------------------")
    print(f"Winner: {winner_candidate}")
    print("-------------------------")
        
        



