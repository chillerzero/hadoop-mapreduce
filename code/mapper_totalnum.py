#!/usr/bin/python

#Find total sales value and number of sales across all stores. Assume 1 reducer

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        value = 1
        print "{0}\t{1}\t{2}".format(store, cost, value)
