#!/usr/bin/python

import sys

# This reducer will find the total sales value and number of sales for each store.

salesTotal = 0
numSales = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue

    thisKey, thisSale, thisCount = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal, "\t", numSales
        oldKey = thisKey
        salesTotal = 0
        numSales = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    numSales += int(thisCount)

if oldKey != None:
    print oldKey, "\t", salesTotal, "\t", numSales
