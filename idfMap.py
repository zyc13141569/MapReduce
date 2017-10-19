#!/usr/bin/env python
import sys
import re

#iterate stdin
for line in sys.stdin:
	line = line.strip()
	print('%s' % line)

	tmp = re.sub(',[\S\t]+', '', line)
	print('%s\t%s' % (tmp, 1))