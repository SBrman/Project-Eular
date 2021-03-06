#! python3

"""
Power digit sum
Problem 16

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

"""

def power_digit_sum(exponent):
    num = str(2**exponent)
    summation = sum((int(digit) for digit in num))
    print(summation)

power_digit_sum(1000)
