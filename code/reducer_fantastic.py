#!/usr/bin/python         

import sys

# Reducer to count up number of times "fantastic" appears

fant_count = long(0)

for line in sys.stdin:
    data_mapped = line.split("\t")
    fant_string, fant_val = data_mapped

    fant_count = fant_count + long(fant_val)

print "Fantastic appears: " + fant_count + " times"
