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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
list_of_Num = []

#part A find all areacode and mobile prefixes called from bangalore


def remove_duplicates(list_of_num):

    list_of_num = list(dict.fromkeys(list_of_num))
    return list_of_num


def findACandMN(unique_list):  # O(5n)

    list_ac_mn = []
    for number in unique_list:  # O(n)
        if '(0' in number:
            i = 0
            while number[i] != ')':  # at worst this loop will run 5 times
                i += 1
            list_ac_mn.append(number[0:i+1])
        if number[0] == '9' or number[0] == '7' or number[0] == '8':
            list_ac_mn.append(number[0:4])
    list_ac_mn = sorted(list(dict.fromkeys(list_ac_mn)))
    return list_ac_mn


def createlistofnumbers(calls):
    for num in range(len(calls)):
        if '(080)' in calls[num][0]:
            list_of_Num.append(calls[num][1])
    unique_list = remove_duplicates(list_of_Num)
    list_final = findACandMN(unique_list)
    return unique_list, list_final




unique_list, list_final = createlistofnumbers(calls)

# Part B
def print_final(list_final):
    for i in list_final:
        print(i)

def PartB(unique_list):
    i = 0.0
    total_calls = len(unique_list)
    for number in unique_list:
        if '(080)' in number:
            i += 1
    percentage = (i/total_calls)*100
    print("%.2f" % percentage + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore. ")


print_final(list_final)
PartB(unique_list)