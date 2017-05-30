from __future__ import division
import math


nSize = 101

print [(a, b, c) for a in range(1, nSize) for b in range(1, nSize) for c in range(1, nSize) if a <= b and a ** 2 + b ** 2 == c ** 2]

l = [(a, b, c) for a in range(1, nSize) for b in range(1, nSize) for c in range(1, nSize) if a <= b]
for n in range(2, 5):
    print "n = ", n
    print [(a, b, c) for a, b, c in l if math.pow(a, n) + math.pow(b, n) == math.pow(c, n)]

