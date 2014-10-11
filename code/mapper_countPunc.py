#!/usr/bin/python

import sys
import csv
def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    puncCount = 0
    for line in reader:
        body = line[4]
        index = len(body)-1
        puncNum = body.count('.') + body.count('!') + body.count('?')
                                                        
        if puncNum == 0:
            writer.writerow(line)
        elif puncNum == 1 and body[index] in ".!?":
            writer.writerow(line)

test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one sentence\n\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    f = open('testfile', 'r')	
    sys.stdin = StringIO.StringIO(f.read())
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
