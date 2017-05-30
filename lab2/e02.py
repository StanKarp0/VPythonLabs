from __future__ import division
import random

s = {0, 1, 2}


def generate_choice(n):
    return [random.choice(list(s)) for i in range(n)]


change = True
win = 0
ch = 0
n = 1000

for choice in generate_choice(n):
    left = s - {choice}
    toShow = random.choice(list(left))
    closed = s - {toShow}
    cross = random.choice(list(closed))

    # print (choice, left, toShow, cross)
    if cross == choice:
        win += 1
    else:
        ch += 1


print (win/n, ch/n)


