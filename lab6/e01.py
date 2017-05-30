from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    n = 10**6
    x_pos = np.zeros(n)
    y_pos = np.zeros(n)


    def new_pos(p, x, y):
        if p <= 0.85:
            return 0.85 * x + 0.04 * y, -0.04 * x + 0.859 * y + 1.6
        elif 0.85 < p <= 0.92:
            return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        elif 0.92 < p <= 0.99:
            return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        else:
            return 0.0, 0.16 * y

    for i in range(n - 1):
        x_pos[i + 1], y_pos[i + 1] = new_pos(np.random.sample(), x_pos[i], y_pos[i])

    plt.figure(facecolor='black')
    plt.subplot(1, 2, 1, axisbg='black')
    plt.plot(x_pos, y_pos, ',', color='Lime')

    xl, xu, yl, yu = 0.25, 0.75, 2, 3
    plt.plot([xl, xu, xu, xl, xl], [yl, yl, yu, yu, yl], 'r')

    x_pos2 = np.zeros(n)
    y_pos2 = np.zeros(n)

    xn, yn = 0.0, 0.0
    cnt = 0
    while cnt < n:
        xn, yn = new_pos(np.random.sample(), xn, yn)
        if xl < xn < xu and yl < yn < yu:
            x_pos2[cnt], y_pos2[cnt] = xn, yn
            cnt += 1

    plt.subplot(1, 2, 2, axisbg='black')
    plt.plot(x_pos2, y_pos2, ',', color='Lime')
    plt.show()

# def border_reflection(pos, vel):
#     vel[np.where(pos < lB)] *= -1
#     vel[np.where(pos > uB)] *= -1
#     f = np.floor(pos / diffB + 0.5)
#     pos = (pos - diffB * f) * np.power(-1.0, f)
#     return pos.copy(), vel.copy()

# def border_reflection(pos, vel):
#     p = np.array(pos)
#     v = np.array(vel)
#     f = np.floor(pos / diffB + 0.5)
#     p = (p - diffB * f) * np.power(-1.0, f)
#     v[np.where(pos < lB)] *= -1
#     v[np.where(pos > uB)] *= -1
#     return vector(p[0], p[1], p[2]), vector(v[0], v[1], v[2])