from __future__ import division
import numpy as np
import math

n = 100000


def probability(dim):
    sums = (np.random.uniform(-1, 1, (n, dim)) ** 2).sum(axis=1)
    return ((sums < 1).real.sum() / n) * (2.0 ** dim)


def factorial_n(x):
    return np.prod(np.arange(1, x + 1))


def factorial_h(x):
    return np.prod(np.arange(3, x + 1, 2) / 2) * (math.sqrt(math.pi)/2)


def v(m):
    f = factorial_n(m/2) if m % 2 == 0 else factorial_h(m)
    l = math.pi ** (m/2)
    return l/f


if __name__ == "__main__":
    with open("file.txt", "w") as file_data:
        res = [(probability(dim), v(dim)) for dim in range(2, 15)]
        toSave = [", ".join([str(r), str(p), str(p / r)]) for p, r in res]
        file_data.write("\n".join(toSave))
