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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create an empty set to store all the different telephone numbers in the records
phone_numbers = set()

# Find all the unique numbers in the texts dataset
for i in range(len(texts)):
    phone_numbers.add(texts[i][0])
    phone_numbers.add(texts[i][1])

# Find all the unique numbers in the calls dataset
for i in range(len(calls)):
    phone_numbers.add(calls[i][0])
    phone_numbers.add(calls[i][1])

# Count all the unique numbers in the records
count_phone_numbers = len(phone_numbers)
print('There are {} different telephone numbers in the records'.format(count_phone_numbers))
