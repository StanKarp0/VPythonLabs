from visual import *
from random import random as rand
import numpy as np

scene = display(width=800, height=600)

bound = 4.0
boxSize = 2 * bound
rad = 0.05

lb = box(pos=(bound, 0, 0), size=(0.1, boxSize, boxSize), color=color.blue)  # lewy
rb = box(pos=(-bound, 0, 0), size=(0.1, boxSize, boxSize), color=color.yellow)# prawy
ub = box(pos=(0, bound, 0), size=(boxSize, 0.1, boxSize), color=color.red) # gorny
bb = box(pos=(0, -bound, 0), size=(boxSize, 0.1, boxSize), color=color.cyan) # dolny
kb = box(pos=(0, 0, -bound), size=(boxSize, boxSize, 0.1), color=color.green) # tylny


def bound_reflection(pos, vel, c):
    if abs(pos.x) + rad > bound:
        c = rb.color if pos.x < 0 else lb.color
        vel.x *= -1
    if abs(pos.y) + rad > bound:
        c = bb.color if pos.y < 0 else ub.color
        vel.y *= -1
    if abs(pos.z) + rad > bound:
        c = kb.color if pos.z < 0 else color.white
        vel.z *= -1
    return pos, vel, c


def vec(a):
    return vector(a[0], a[1], a[2])


nSph = 500
rBound = bound - 2 * rad
position = np.random.random((nSph, 3)) * 2 * rBound - rBound
velocity = (np.random.random((nSph, 3)) - 0.5)/100.0
sph = [sphere(pos=vec(position[i, :]), color=color.white, radius=rad, vel=vec(velocity[i, :])) for i in range(nSph)]

t, dt, tEnd = 0, 0.005, 1000
while t < tEnd:
    rate(1000)
    for s in sph:

        s.pos, s.vel, s.color = bound_reflection(s.pos, s.vel, s.color)
        s.pos += s.vel
    t += dt





