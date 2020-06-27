#! python3

"""
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

https://projecteuler.net/project/images/p015.png

How many such routes are there through a 20×20 grid?

"""

from pprint import pprint
from itertools import permutations
import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def routes(ROW, COLUMN):

    combo_normal = ['DOWN'] * ROW + ['RIGHT'] * COLUMN
    for i, _ in enumerate(set(permutations(combo_normal, ROW + COLUMN)), 1):
        if i % 1000000 == 0:
            print(i)
    return i

num = 6
r = routes(ROW=num, COLUMN=num)
print(r)
