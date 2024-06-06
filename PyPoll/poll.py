# import and read dataset

import pandas as pd
file_path = 'Resources/election_data.csv'
df = pd.read_csv(file_path)

# print

print(" ")
print("Election Results")
print("-------------------------")

## calculations

# total number of votes cast

total_votes = df['Ballot ID'].count()
print(f"Total Votes: {total_votes}")
print("-------------------------")

# complete list of candidates who received votes

number_candidates = df['Candidate'].nunique()
candidate = df['Candidate'].unique()
candidate_list = candidate.tolist()

## I am purposefully using a for loop so that potentially if this dataset
## had way more than three candidates, this code could still apply

# percentage and number of votes each candidate won
# put percentages into new list to calculate winner later

df['Percentage'] = ""

for i in range(number_candidates):
    candidate_count = (df['Candidate'] == candidate_list[i]).sum()
    candidate_percentage = candidate_count / total_votes
    percentage = "{:.3%}".format(candidate_percentage)
    print(f"{candidate_list[i]}: {percentage} ({candidate_count})")

    df.iloc[i, df.columns.get_loc('Percentage')] = percentage

# winner of election based on popular vote
winner_index = df['Percentage'].idxmax()
winner = candidate_list[winner_index]
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



