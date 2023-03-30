#!/usr/bin/python

import sys

# initialize variables
old_street_code = None
violation_count = 0

# read the input from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    street_code, violation_type = line.split('\t', 1)
    # check if we are still processing the same street code
    if old_street_code and old_street_code != street_code:
        # output the result
        print('%s\t%s' % (old_street_code, violation_count))
        # reset the variables
        old_street_code = street_code
        violation_count = 0
    # process the data
    old_street_code = street_code
    if violation_type == "Ticket":
        violation_count += 1

# output the last result
if old_street_code != None:
    print('%s\t%s' % (old_street_code, violation_count))