# pole kola (0, 0) r=1, kw x= (-1,1) y=(-,1)
from __future__ import division
import random
import math


def rand_sq():
    return random.uniform(-1, 1), random.uniform(-1, 1)


def contains(p):
    x, y = p
    return x ** 2 + y ** 2 < 1

ls = []
res = []
for i in range(1, 100) + [10 ** j for j in range(1, 7)]:
    n2add = i - len(ls)
    ls += [rand_sq() for x in range(n2add)]
    n0 = sum(1 for x in ls if contains(x))
    res.append((len(ls), n0/len(ls)))

with open("pi.txt", "w") as file_data:
    for r in res:
        size, m = r
        s = (4 * m)/math.pi
        file_data.write(str(size) + " " + str(math.pi) + " " + str(4*s)+" " + str(s) + "\n")


# dc