#!/usr/bin/python3
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
infile = sys.argv[1] if len(sys.argv)>1 else '16day.in'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]
print(lines)

