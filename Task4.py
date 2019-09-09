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

def return_list_of_number():
    listnum = []
    for row in calls:
        listnum.append(row[0])

    listnum = list(dict.fromkeys(listnum))
    return listnum

def check_lists(listnum):
    for num in listnum:
        for row in calls:
            if row[1] in listnum:
                listnum.remove(row[1])
    for num in listnum:
        for row in texts:
            if row[0] in listnum:
                listnum.remove(row[0])
    for num in listnum:
        for row in texts:
            if row[1] in listnum:
                listnum.remove(row[1])

    return listnum

def teleMark_nums(calls):
    uniqueNo = return_list_of_number()
    listnum = check_lists(uniqueNo)
    return listnum

def print_main():
    listFinal = teleMark_nums(calls)
    listFinal.sort()
    print("These numbers could be telemarketers: ")
    for i in listFinal:
        print(i)
    return 0
print_main()

