from __future__ import division
import math


def func(x):
    return 50 * math.sin(x)

x_args = [(2 * x * math.pi)/50 for x in range(51)]
y_args = [func(x) for x in x_args]
y_min, y_max = min(y_args), max(y_args)

y_lines = [y for y in range(25, -25, -1)]
scale = 50/(y_max - y_min)


def symbol(y, y_line):
    ys = y * scale
    if ys < y_line < 0:
        return "-"
    elif ys > y_line > 0:
        return "+"
    elif int(ys) == 0 and y_line == 0:
        return "0"
    else:
        return " "

with open("file2.txt", "w") as file_data:
    points = [[symbol(y, y_line) for y in y_args] for y_line in y_lines]
    lines = ["".join(l) for l in points]
    file_data.write("\n".join(lines))
