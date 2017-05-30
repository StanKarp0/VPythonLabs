from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

n = 10000
p = 15

for i in range(p):
    alpha = np.random.random((n, 1)) * np.pi * 2.0
    sinAlpha = np.sin(alpha)
    cosAlpha = np.cos(alpha)
    xArray = np.zeros((n, 1))
    yArray = np.zeros((n, 1))
    index = 0
    for j in range(n - 1):
        xArray[j+1] = xArray[j] + cosAlpha[j]
        yArray[j+1] = yArray[j] + sinAlpha[j]
    plt.plot(xArray, yArray, lw=0.15)
    plt.plot(xArray[-1:], yArray[-1:], 'ok', ms=10)
plt.show()
