from __future__ import division
import math


def func(x):
    return 50 * math.sin(x)

x_args = [(2 * x * math.pi)/50 for x in range(51)]
y_args = [func(x) for x in x_args]
y_lines = [y for y in range(30, -30, -1)]


def line(y, y_cord):
    if y < y_cord < 0:
        return "-"
    elif y > y_cord > 0:
        return "+"
    elif int(y) == 0 and y_cord == 0:
        return "0"
    else:
        return " "

with open("file2.txt", "w") as file_data:
    points = [[line(func(x)/2, y_cord) for x in x_args] for y_cord in range(30, -30, -1)]
    lines = ["".join(l) for l in points]
    file_data.write("\n".join(lines))


