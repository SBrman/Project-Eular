#! python3

"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def primesBelow(number):
    # Sieve of Erastothenes

    #[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    primes = [0, 0] + [1,]*(number-1)

    position = 2
    while position**2 < number:
        if primes[position] == 1:
            for i in range(position*2, number+1, position):
                primes[i] = 0

        position += 1

    summation = 0
    for number, isPrime in enumerate(primes):
        if isPrime:
            summation += number
    return summation
    
print(primesBelow(2000000))
