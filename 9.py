#! python3

"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def intCheck(num):
    if str(num)[-2:] == '.0':
        return True
    return False

def abc(number=1000):        
    for a in range(1, number):
        for b in range(1, number):
            if a < b:
                c = (a**2 + b**2)**(0.5)
                if intCheck(c):
                    c = int(c)
                    if a+b+c == number:
                        return a*b*c
print(abc())
