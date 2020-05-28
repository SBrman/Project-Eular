#! python3

"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import logging

#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.INFO, format='%(message)s')

def isPrime(num):
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def primeFactor(number, factors=[]):
    
    if isPrime(number):
        factors.append(number)
        logging.info(factors)
        return factors

    for i in range(2, number):
        if isPrime(i):
            if number % i == 0:
                factors.append(i)
                logging.info(factors)
                number = int(number / i)
                logging.info('recursion')
                primeFactor(number)
                return factors
    
print(max(primeFactor(600851475143)))
