"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import Task1


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Steps:

# Get the list of unique numbers from task 1

ListOfUniqueNo, column_search = Task1.task1()
callDuration = 0

# Create a map of Unique numbers initialize the value to 0 this is placeholder to add time spent on call
map_numbers = dict.fromkeys(ListOfUniqueNo, callDuration)

# Update the existing Key value with the sum of prev value + next value

def task2_Opt(ListOfUniqueNo,column_search): # O(2n)
    for i in range(column_search):
        for row in calls:
            if row[i] in map_numbers.keys():
                x = map_numbers[row[i]]
                x = x + int(row[3])
                map_numbers.update({row[i]: x})
        # iterate the map of those numbers and store the max time duration and respective Ph number
    phNumber = list(map_numbers.keys())
    time_spent = list(map_numbers.values())
    #print(map_numbers)
    print(str(phNumber[time_spent.index(max(time_spent))]) + ' spent the longest time, ' + str(
            max(time_spent)) + ' seconds, on the phone during September 2016.')

task2_Opt(ListOfUniqueNo,column_search)