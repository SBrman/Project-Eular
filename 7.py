#! python3

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

"""

def isPrime(number):
    if number == 0 or number == 1:
        return False
    if number == 2:
        return True
    
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def nthPrime(nthNumber):
    n = 0
    i = 1
    while True:
        if isPrime(i):
            n += 1

        if n == nthNumber:
            print(i)
            break
        
        i+=1

nthPrime(10001)
