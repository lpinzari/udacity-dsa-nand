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

# last record index in calls.csv
last = len(calls)-1

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print('First record of texts, {} texts {} at time {}'.format(texts[0][0],texts[0][1],texts[0][2]))

print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(calls[last][0],calls[last][1],calls[last][2],calls[last][3]))
