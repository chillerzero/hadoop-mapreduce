#!/usr/bin/python

import sys

# This reducer will find the total sales value and number of sales for each store.

salesTotal = 0
numSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisKey, thisSale, thisCount = data_mapped

    salesTotal += float(thisSale)
    numSales += long(thisCount)

print "Total Sales Value:", "\t", salesTotal, "Total Sales Number:", "\t", numSales
