#!/usr/bin/python

import sys

# Mapper for number of hits to page

link = "http://www.the-associates.co.uk"

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, ident, user, time, zone, method, path, qstring, status, size = data
        value = 1
        if (path[:31] == link):
            path = path[31:]
        print "{0}\t{1}".format(path, value)