"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import Task3

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def teleMark_nums(calls):
    listnum = []
    for row in calls:
        #print(row[0])
        number = row[0]
        if '140' in number[0:3]:
            #print(row[0])
            listnum.append(row[0])
    #print(len(listnum))
    return listnum
print("These numbers could be telemarketers: ")

Task3.print_final(teleMark_nums(calls))