"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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

# Create an empty dictionary to store all the telephone numbers (key) and the total duration in seconds of the telephone numbers' calls (value).
timeSpentOnPhone = {}

# Compute the total duration of the telephone numbers' calls. If a number is already included in the dictionary, add the duration of the phone call. If not, add the number to the dictionary and set its value to the phone call's duration.
for i in range(len(calls)):
    call_duration = int(calls[i][3])
    # calling number
    if calls[i][0] not in timeSpentOnPhone:
        timeSpentOnPhone[calls[i][0]] = call_duration
    else:
        timeSpentOnPhone[calls[i][0]] += call_duration
    # receiving number
    if calls[i][1] not in timeSpentOnPhone:
        timeSpentOnPhone[calls[i][1]] = call_duration
    else:
        timeSpentOnPhone[calls[i][1]] += call_duration

# Find the phone number with the longest calls duration
max_calls_duration = 0
phone_max_duration = None

# Find the first key which has the maximum value.
for key in timeSpentOnPhone:
    if timeSpentOnPhone[key] > max_calls_duration:
        max_calls_duration = timeSpentOnPhone[key]
        phone_max_duration = key

print('{} spent the longest time, {} seconds, on the phone during September 2016'.format(phone_max_duration,max_calls_duration))
