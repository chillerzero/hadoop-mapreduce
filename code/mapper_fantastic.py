#/usr/bin/python

import sys
import csv

def mapper():

    reader = csv.reader(sys.stdin, delimiter=' \t.,!?:;\"()<>[]#$=-/')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for token in reader:
        data = line.strip()
        if data.lower() == 'fantastic':
            token = token + "\t" + 1
            writer.writerow(token)

def main():
    import StringIO
    f = open('testforum.tsv','r')
    sys.stdin = StringIO.StringIO(f.read())
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
