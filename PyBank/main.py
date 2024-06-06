import pandas as pd

# path to CSV file
file_path = 'Resources/budget_data.csv'

# load CSV into DataFrame
df = pd.read_csv(file_path)

## calculations

# number of months
month_count = df['Date'].count()

# net total profit/losses
net_total = df['Profit/Losses'].sum()

# calculate changes in profit and put in new column
df['Change'] = None
for i in range(1, month_count):
    df.iloc[i, df.columns.get_loc('Change')] = df.iloc[i]['Profit/Losses'] - df.iloc[i-1]['Profit/Losses']

# average change
average_change = df['Change'].mean()
formatted_average_change = "{:.2f}".format(average_change)

# greatest increase in profits
greatest_increase = df['Change'].max()
greatest_increase_date = df.loc[df['Change'] == greatest_increase, 'Date'].values[0]

# greatest decrease in profits
greatest_decrease = df['Change'].min()
greatest_decrease_date = df.loc[df['Change'] == greatest_decrease, 'Date'].values[0]

# print results
print(" ")
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${formatted_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print(" ")

# print dataset just for reference
print("Dataset including new column for 'Change' can be seen below.")
print(" ")
print(df)

