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

def get_possible_Telemarketers():
    
    not_possible_Telemarketers = set()
    possible_Telemarketers = set()

    # Telemarketers never send or receive texts
    for i in range(len(texts)):
        not_possible_Telemarketers.add(texts[i][0])
        not_possible_Telemarketers.add(texts[i][1])

    # Telemarketers never receive incoming calls
    for i in range(len(calls)):
        not_possible_Telemarketers.add(calls[i][1])

    for i in range(len(calls)):
        if calls[i][0] not in not_possible_Telemarketers:
            possible_Telemarketers.add(calls[i][0])

    return list(possible_Telemarketers)

possible_Telemarketers = get_possible_Telemarketers()
possible_Telemarketers.sort()

print('These numbers could be telemarketers:')
for number in possible_Telemarketers:
    print(number)
