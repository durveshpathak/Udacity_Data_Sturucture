"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
#import Task3

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
            #print(row)
            if row[1] in listnum:
                #print('Found')
                listnum.remove(row[1])
                #print('not found')
    for num in listnum:
        for row in texts:
            if row[0] in listnum:
                #print('Found')
                listnum.remove(row[0])
                #print('not found')
    for num in listnum:
        for row in texts:
            if row[1] in listnum:
                #print('Found')
                listnum.remove(row[1])
                #print('not found')

    return listnum

def teleMark_nums(calls):
    uniqueNo = return_list_of_number()
    #print(len(uniqueNo))
    listnum = check_lists(uniqueNo)
    #print(len(listnum))
    return listnum

def print_main():
    listFinal = teleMark_nums(calls)
    listFinal.sort()
    print("These numbers could be telemarketers: ")
    for i in listFinal:
        print(i)
    return 0
print_main()

