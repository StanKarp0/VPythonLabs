from __future__ import division
from visual import *
import numpy as np
import numpy.linalg as lin


def a2v(arr):
    return vector(arr[0], arr[1], arr[2])

scene = display(width=800, height=600)

G = 6.7 * 10**-11
R = 10**10
m_sun = 2 * 10**30
mld = 10**9
km = 10**3
dt = 1000.

p_radius = 5.
s_radius = 15.
n_planets = 4
p_shape = (n_planets, 3)
pos = np.zeros(p_shape)
pos[:, 0] = np.array([70., 110., 150., 240.]) * mld

vel = np.zeros(p_shape)
vel[:, 1] = np.array([47., 35., 30., 24.]) * km

acc = np.zeros(p_shape)

sun = sphere(pos=(0, 0, 0), color=color.yellow, radius=3*R)
planets = [sphere(pos=a2v(r), radius=R, make_trail=True, trail=curve(pos=[r])) for r in pos]

planets[0].color = color.orange
planets[1].color = color.white
planets[2].color = color.blue
planets[3].color = color.red
planets[0].trail.color = color.orange
planets[1].trail.color = color.white
planets[2].trail.color = color.blue
planets[3].trail.color = color.red

while True:
    rate(10000)
    acc = (-G * m_sun * pos) / np.power(lin.norm(pos, axis=1), 3.).reshape((n_planets, 1))
    vel += acc * dt
    pos += vel * dt

    for r, p in zip(pos, planets):
        p.pos = r
        p.trail.append(pos=r)

