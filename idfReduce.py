#!/usr/bin/env python
import sys
import re
import math

currentWord = None
word = None
totalDoc = 20
doccount = 1
#read input
#input format : word,doc\tcount
for line in sys.stdin:
	line = line.strip()
	# print(line)

	word, count = line.split('\t', 1)
	# print("after : " + word)
	try:
		count = int(count)
	except ValueError:
		continue

	if(re.match('\S+,\S+', word)):
		# print(word)
		result = count * math.log(float(totalDoc) / float(doccount))
		print('%s\t%s' % (word, result))
	else:
		if currentWord == word:
			doccount += count
		else:
			doccount = count
			currentWord = word
