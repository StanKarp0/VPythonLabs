from __future__ import division
import math


def func(x):
    return 50 * math.sin(x)

x_args = [(2 * x * math.pi)/50 for x in range(51)]
y_args = [func(x) for x in x_args]

center = 50

min_y, max_y = min(y_args), max(y_args)
diff = max_y - min_y
scale = (center * 2)/diff


def line(ys):
    if ys == 0:
        return " " * center + "0"
    elif ys > 0:
        return " " * (center+1) + "+" * ys
    else:
        return " " * (center + ys) + "-" * (-ys)

with open("file.txt", "w") as file_data:
    file_data.write("\n".join([line(int(scale * y)) for x, y in zip(x_args, y_args)]))
