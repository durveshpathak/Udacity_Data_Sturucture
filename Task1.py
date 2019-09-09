"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1: O(2n^2 +1)
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def task1():
    total_entry = []
    column_search = 2
# Steps:
# create a list of all found entries in column 1 & 2 of texts and lists. O(n^2)
    for i in range(column_search):
        for j in range(len(texts)):
            total_entry.append(texts[j][i])

    for i in range(column_search):
        for j in range(len(calls)):
            total_entry.append(calls[j][i])

# Remove duplicates from the list.

    total_entry = list(dict.fromkeys(total_entry))

    return total_entry, column_search


total_entry,column = task1()
print('There are ' + str(len(total_entry)) + ' different telephone numbers in the records.')

