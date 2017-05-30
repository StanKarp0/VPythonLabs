from __future__ import division
import random

l = [0, 1, 2]


def generate_choice():
    choice = random.choice(l)
    cross = random.choice(l)
    show = random.choice(list(set(l) - {choice, cross}))
    return choice, cross, show


def generate_choice_list(n):
    return [generate_choice() for _ in range(n)]


def calc_no_change(n):
    def red(cnt, (choice, cross, _)):
        return (cnt + 1) if choice == cross else cnt
    return reduce(red, generate_choice_list(n), 0)/n


def calc_change(n):
    def red(cnt, (choice, cross, show)):
        choice = (set(l) - {choice, show}).pop()
        return (cnt + 1) if choice == cross else cnt
    return reduce(red, generate_choice_list(n), 0)/n


print calc_no_change(1000)
print calc_change(1000)
