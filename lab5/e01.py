from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# 2 do 365


def test_dim(n, dim):
    p = np.random.randint(1, 366, n)
    eq = p == p[:, np.newaxis]
    return (dim - 1) in np.sum(eq - np.identity(n), axis=0)


def calc_dim(n, tests, dim):
    g = np.array([test_dim(n, dim) for _ in range(tests)])
    return g.sum()/tests


def calc(dim):
    x = np.arange(2, 365)
    y = np.array([calc_dim(n, 200, dim) for n in x])
    plt.plot(x, y, label="n ="+str(dim))
    np.savetxt("file" + str(dim) + ".txt", np.array(zip(x, y)))
    print "done "+str(dim)

if __name__ == "__main__":

    calc(2)

    calc(3)

    calc(4)

    plt.title("Wykres prawdopodobienstwa")
    plt.xlabel("Liczba osob")
    plt.ylabel("Prawdopodobienstwo")
    plt.axis([0, 366, -0.25, 1.25])
    plt.grid()
    plt.show()

# def x_new_coord(prop, x, y):
# 	x_new = 0.
# 	if (prop <= 0.85):
# 		x_new = 0.85*x + 0.04*y
# 	elif(prop > 0.85 and prop <= 0.92):
# 		x_new = 0.2*x-0.26*y
# 	elif(prop > 0.92 and prop <= 0.99):
# 		x_new = -0.15*x + 0.28*y
# 	else:
# 		x_new = 0.
# 	return x_new
#
#
# def y_new_coord(prop, x, y):
# 	y_new = 0.
# 	if (prop <= 0.85):
# 		y_new = -0.04*x + 0.85*y + 1.6
# 	elif(prop > 0.85 and prop <= 0.92):
# 		y_new = 0.23*x+0.22*y + 1.6
# 	elif(prop > 0.92 and prop <= 0.99):
# 		y_new = 0.26*x + 0.24*y + 0.44
# 	else:
# 		x_new = 0.16*y
# 	return y_new