#!/usr/bin/python

import sys
import csv

def mapper():

    reader = csv.reader(sys.stdin, delimiter=' \t.,!?:;\"()<>[]#$=-/')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for token in reader:
        data = line.strip()
        if data.lower() == 'fantastic':
            writer.writerow(token)
