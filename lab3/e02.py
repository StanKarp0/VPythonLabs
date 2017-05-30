import random
import time
bmin, start, bmax = 0, 50, 100
print " " * start + "start"


def mutate(pos):
    return pos + random.choice([-1, 1])
act = start
step = 0
while bmin <= act <= bmax:
    print " " * act + "*" + str(act - start) + "(" + str(step) + ")"
    act = mutate(act)
    step += 1
    #time.sleep(0.1)
print step


