#!/usr/bin/python

import sys

# Find monetary value for highest individual sale for each separate store

highestSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSale
        oldKey = thisKey
        highestSale = 0

    oldKey = thisKey
    
    if highestSale < thisSale:
        highestSale = thisSale

if oldKey != None:
    print oldKey, "\t", highestSale
