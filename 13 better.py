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

os.chdir(r'H:\python\Project Eular')
with open('13.txt', 'r') as file:
    text = [line.strip() for line in file.readlines()]

extra = 0
counter = []

for i in range(len(text[0]) - 1, -1, -1):
    summation = 0
    for line in text:
        summation += int(line[i])
    summation += extra
    counter.append(str(str(summation)[-1]))
    extra = int(str(summation)[:-1])

counter.append(str(extra))
counter.reverse()
counter = ''.join(counter)

print(counter[:10])
