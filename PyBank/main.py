import os
import csv

# path to CSV file
file_path = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# read CSV file
with open(file_path, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    ## calculations
    month_count = 0
    date_list = []
    net_total = 0
    change_list = []
    greatest_increase = 0
    prev_profit = None

    for row in csv_reader:

        # number of months
        month_count = month_count + 1
        date = row[0]
        date_list.append(date)

        # net total profit/losses
        net_total = net_total + int(row[1])

        # calculate changes in profit
        current_profit = int(row[1])
        if prev_profit is None:
            change = 0
            change_list.append(change)
        else:
            change = current_profit - prev_profit
            change_list.append(change)
        prev_profit = current_profit

    # average change
    average_change = sum(change_list) / (len(change_list)-1)
    formatted_average_change = "{:.2f}".format(average_change)

    # greatest increase in profits
    greatest_increase = max(change_list)
    greatest_increase_index = change_list.index(greatest_increase)
    greatest_increase_date = date_list[greatest_increase_index]

    # greatest decrease in profits
    greatest_decrease = min(change_list)
    greatest_decrease_index = change_list.index(greatest_decrease)
    greatest_decrease_date = date_list[greatest_decrease_index]

# print results
print("")
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${formatted_average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
print("")

# print dataset just for reference
