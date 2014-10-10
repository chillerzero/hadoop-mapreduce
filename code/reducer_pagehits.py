#!/usr/bin/python

import sys

# Reducer to add up page hits

pagehits = long(0)
oldPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisPage, thisCount = data_mapped

    if oldPage and oldPage != thisPage:
        print oldPage, "\t", pagehits
        oldPage = thisPage
        pagehits = long(0)

    oldPage = thisPage
    pagehits += long(thisCount)

if oldPage != None:
    print oldPage, "\t", pagehits
