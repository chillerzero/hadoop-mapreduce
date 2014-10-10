#!/usr/bin/python

import sys

# Reducer to add up page hits

pagehits = long(0)
oldIp = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisIp, thisCount = data_mapped

    if oldIp and oldIp != thisIp:
        print oldIp, "\t", pagehits
        oldIp = thisIp
        pagehits = long(0)

    oldIp = thisIp
    pagehits += long(thisCount)

if oldIp != None:
    print oldIp, "\t", pagehits
