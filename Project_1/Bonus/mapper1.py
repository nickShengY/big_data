#!/usr/bin/python

import sys

# read the input from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split(",")
    # parse the data
    street_code = words[0]
    violation_type = words[1]
    # output key-value pairs
    print('%s\t%s' % (street_code, violation_type))

