from visual import *
from random import random as rand

scene = display(width=800, height=600)

bound = 4.0
boxSize = 2 * bound
rad = 0.8

lb = box(pos=(bound, 0, 0), size=(0.3, boxSize, boxSize), color=color.blue)  # lewy
rb = box(pos=(-bound, 0, 0), size=(0.3, boxSize, boxSize), color=color.yellow)# prawy
ub = box(pos=(0, bound, 0), size=(boxSize, 0.3, boxSize), color=color.red) # gorny
bb = box(pos=(0, -bound, 0), size=(boxSize, 0.3, boxSize), color=color.cyan) # dolny
kb = box(pos=(0, 0, -bound), size=(boxSize, boxSize, 0.3), color=color.green) # tylny


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

position = vector(0.0, 0.0, 0.0)
velocity = vector(rand() - 0.5, rand() - 0.5, rand() - 0.5)/50.0

sph = sphere(pos=position, color=color.white, radius=rad, vel=velocity, make_trail=True)

t, dt, tEnd = 0, 0.005, 1000
while t < tEnd:
    rate(1000)
    sph.pos += sph.vel
    sph.pos, sph.vel, sph.color = bound_reflection(sph.pos, sph.vel, sph.color)
    t += dt





