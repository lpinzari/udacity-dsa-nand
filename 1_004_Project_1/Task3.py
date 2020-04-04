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


#-------------------- Part A -----------------------#

# Supporting function

def get_area_code(call_number):
    """
        This function get the area code (fixed-line, Telemarketers,mobile) of a call number
        Args:
            (string) call_number - a string representing a call number
        Returns:
            (string) - the area code
        Note:
            If the number is not in the specifications categories returns None
    """

    # fixed-line
    if call_number.startswith('(0'):
        return call_number.split(')')[0]+')'

    # Telemarketers
    if call_number.startswith('140'):
        return '140'

    # Mobile
    if (' ' in call_number) and (call_number.startswith('7') or call_number.startswith('8') or call_number.startswith('9')):
        return call_number[:4]

    print('Not found')
    return None


# Create a set to store all the area codes and mobile prefixes called by peopele in Bangalore
bang_called_codes = set()

# Find all the area codes
for i in range(len(calls)):
    if calls[i][0].startswith('(080)'):
        bang_called_codes.add(get_area_code(calls[i][1]))

bang_called_codes_list = list(bang_called_codes)
bang_called_codes_list.sort()
print('The numbers called by people in Bangalore have codes:')

for called_code in bang_called_codes_list:
    print(called_code)


#-------------------- Part B -----------------------#


count_bang_to_others = 0
count_bang_to_bang = 0

# Count all the calls made from a fixed line in Bangalore and all the calls from a fixed line in Bangalore to a fixed line also in Bangalore.

for i in range(len(calls)):
    if calls[i][0].startswith('(080)'):
        count_bang_to_others += 1
        if calls[i][1].startswith('(080)'):
            count_bang_to_bang += 1

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(round(count_bang_to_bang/count_bang_to_others*100),2))
