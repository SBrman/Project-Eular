#! python3

"""
Large sum
Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

37107287533902102798797998220837590246510135740250
...
53503534226472524250874054075591789781264330331690
"""

import os
from pprint import pprint
os.chdir('H:\python\Project Eular')

with open('13.txt', 'r') as file:
    numbers = file.readlines()

numbers = [line.strip('\n') for line in numbers]
##
##n = 0
##
##for number in numbers:
##    n += int(number)
##
##print(str(n)[:10])

print(str(sum([int(number) for number in numbers]))[:10])
