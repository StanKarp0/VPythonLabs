from __future__ import division
import numpy as np
from visual import *


def _minus(arr):
    return arr - arr.reshape(arr.shape[0], 1, 3)


def _dist3d(arr):
    return np.sqrt(np.sum(np.power(arr, 2.), 2))


def _distance(arr):
    return np.sqrt(np.sum(np.power(arr, 2.), 1))

R_ring = 10.
r_ball = 0.2
R_ball = 1.
m_ball = 1.
M_ball = 10.
n_sph = 30  # Liczba kulek
r_shape = (n_sph, 3)
thk = 0.05

# Wyswietlanie dekoracji
sphere(radius=R_ring, opacity=0.2)
curve(pos=[(0, 0, 0), (R_ring+2, 0, 0)])
curve(pos=[(0, 0, 0), (0, R_ring+2, 0)])
curve(pos=[(0, 0, 0), (0, 0, R_ring+2)])
ring(pos=(0, 0, 0), axis=(0, 0, 1), radius=R_ring+thk/2., thickness=thk)
ring(pos=(0, 0, 0), axis=(0, 1, 0), radius=R_ring+thk/2., thickness=thk)
ring(pos=(0, 0, 0), axis=(1, 0, 0), radius=R_ring+thk/2., thickness=thk)

# Losowanie pozycji wspolrzedne sferyczne
ta1 = np.random.random(n_sph) * 2 * np.pi
ta2 = np.random.random(n_sph) * 2 * np.pi
tr = np.random.random(n_sph) * (R_ring - 1) - (R_ring - 1)

# Przejscie do wspolrzednych xyz
x = tr * np.cos(ta1) * np.cos(ta2)
y = tr * np.cos(ta1) * np.sin(ta2)
z = tr * np.sin(ta1)

# Wartosci poczatkowe
r = np.array([x, y, z]).T
v = (np.random.random(r_shape)-0.5) * 0.02
R = np.ones(n_sph) * r_ball
m = np.ones(n_sph) * m_ball

# Oznaczenie pierwszej duzej kulki
R[0] = R_ball
r[0, :] = 0.
v[0, :] = 0.
m[0] = M_ball

R_sum = R + R[:, np.newaxis]
R_sum2 = np.power(R_sum, 2.0)

balls = [sphere(color=color.red, radius=rad) for rad in R]
balls[0].color = color.blue

dt = 0.2

while 1:
    rate(10000)

    for ball, pos in zip(balls, r):
        ball.pos = pos

    r_next = r + v * dt

    # Odbicie od granicy
    r_dist_next = _distance(r_next) + R
    r_dist_b = r_dist_next >= R_ring

    r_b = r[r_dist_b, :]/R_ring
    if r_b.shape[0]:
        r_reshape = np.repeat(np.sum(v[r_dist_b] * r_b, 1), [3]).reshape(r_b.shape)
        v_r = r_reshape * r_b
        v[r_dist_b] -= 2 * v_r

    # Odbicie kulek
    r_m = _minus(r_next)
    v_m = _minus(v)
    r_dist = _dist3d(r_m)

    a = np.power(_dist3d(v_m), 2.0)
    b = np.sum(2.0 * r_m * v_m, 2)
    c = np.power(r_dist, 2.0) - R_sum2
    delta = np.power(b, 2.) - 4 * a * c

    # Spelnienie warunkow na odbiecie kulek
    dtp_c = ((delta > 0) * (a != 0) * (r_dist <= R_sum)) > 0

    # Rozwiazanie (-b - sqrt(c))/(2a)
    dt_res = (-b[dtp_c] - np.sqrt(delta[dtp_c])) / (2 * a[dtp_c])
    dt_p = np.ones((n_sph, n_sph)) * (-dt)
    dt_p[dtp_c] = (-b[dtp_c] - np.sqrt(delta[dtp_c])) / (2 * a[dtp_c])

    # Wyznaczenie nie powtarzajacych sie par (stad macierz trojkatna dolna - tri) kulek do odbicia od siebie
    dtp_i, dtp_j = np.where((dt_p > -dt) * np.tri(n_sph, k=-1))
    pairs = np.array([dtp_i, dtp_j]).T

    if pairs.shape[0]:
        v1, v2 = v[pairs[:, 0]], v[pairs[:, 1]]
        r1, r2 = r[pairs[:, 0]], r[pairs[:, 1]]
        m1, m2 = m[pairs[:, 0]], m[pairs[:, 1]]

        r1mr2 = r1 - r2
        m1pm2 = m1 + m2
        p1 = r1mr2 / np.sqrt(np.sum(np.power(r1mr2, 2.0)))
        p2 = np.sum((v1 - v2) * p1) * p1
        mw1 = np.repeat(m2 / m1pm2, [3]).reshape(v1.shape)
        mw2 = np.repeat(m1 / m1pm2, [3]).reshape(v1.shape)
        v[pairs[:, 0]] = v1 - 2 * mw1 * p2
        v[pairs[:, 1]] = v2 + 2 * mw2 * p2

    r += v * dt
