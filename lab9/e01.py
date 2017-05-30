from __future__ import division
from visual import *
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

rad = 0.4
length = 100.
n_balls = 49
dt = 0.001
k = 100.
m = 1.
g = np.array([0, -9.81, 0])
alpha = 0.25

scene = display(
    width=1350,
    height=500.,
    center=(length/2., 0, 0)
)

n_shape = (n_balls + 2, 3)
force = np.zeros(n_shape)
velocity = np.zeros(n_shape)
position = np.zeros(n_shape)
position[:, 0] = np.linspace(0, length, n_balls+2)
axis = position[1:, :] - position[:-1, :]
axis_org = axis

position[1, 1] = 15.
# position[-2, 1] = -10.

balls = [sphere(radius=rad, color=color.red) for _ in range(n_balls+2)]
balls[0].visible = False
balls[-1].visible = False
helices = [helix(radius=rad, color=color.green, thickness=0.1) for _ in range(n_balls+1)]
box(pos=(0, 0, 0), size=(0.3, 5., 5.))
box(pos=(length, 0, 0), size=(0.3, 5., 5.))

i, i_max = 0, 5000
force_k = np.zeros((i_max, 1))
force_v = np.zeros((i_max, 1))

while i < i_max:
    rate(100)

    for ball, pos in zip(balls, position):
        ball.pos = pos

    for h, pos, ax in zip(helices, position, axis):
        h.pos = pos
        h.axis = ax

    force[1:-1, :] = k * (position[2:, :] + position[:-2, :] - 2*position[1:-1, :])
    force[1:-1, :] += g * m
    # force += - alpha * velocity

    velocity += (force/m) * dt
    position += velocity * dt
    axis = position[1:, :] - position[:-1, :]

    force_k[i] = (k/2.)*np.sum(np.power(norm(axis_org, axis=1)-norm(axis, axis=1), 2.0))
    force_v[i] = m * np.sum(np.power(norm(velocity, axis=1), 2.))/2.
    i += 1

x_iter = np.arange(0, i_max)
plt.plot(x_iter, force_k)
plt.plot(x_iter, force_v)
plt.plot(x_iter, force_k + force_v)
plt.show()
