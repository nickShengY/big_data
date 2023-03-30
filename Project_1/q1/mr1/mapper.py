#!/usr/bin/python
import sys
import csv

for line in csv.reader(iter(sys.stdin.readline, '')):
    time = line[19]
    if time and time[0] != 'V' and len(time) == 5:
        hour = time[:-3] + '00' + time[4]
        print("{0}\t1".format(hour))


