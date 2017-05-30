from __future__ import division
import random

s = [0, 1, 2]


def generate_choice(n):
    return [random.sample(s, 2) for i in range(n)]

change = False
n = 10000
s1 = 0
s2 = 0
for x in generate_choice(n):
    win = random.randint(0, 2)
    ch = random.randint(0, 2)

    left = set(s) - {ch}
    dropped = random.choice(list(left))

    gates = list(left)
    gates.remove(dropped)

    if dropped == win:
        choice = win
    else:
        choice = gates[0]

    if win == choice:
        s1 += 1
    else:
        s2 += 1


print s1/n
print s2/n
