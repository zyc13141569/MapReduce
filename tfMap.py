#!/usr/bin/env python

import sys
import re
import os

fileName = os.environ['mapreduce_map_input_file']
fName = re.sub(r'(^.*Gutenberg/)', '', fileName)
# input comes from STDIN (standard input)
#fName = "book2"
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = filter(None, re.split('[\W+_]', line))
    # write out word paired with count of 1
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is
        print('%s,%s\t%s' % (word.lower(), fName, 1))
