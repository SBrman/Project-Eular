#! python3

"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""
def isPrime(number):
    if number == 0 or number ==1:
        return False
    if number == 2:
        return True
    
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def multiplyByWhat(number, dividerNum):
    if isPrime(dividerNum):
        return dividerNum
    else:
        for i in range(2,dividerNum):
            if (number*i) % dividerNum == 0:
                multiplier = i
                return multiplier
                
def divisableByAllNumbers(uptoNum=10):
    number = 1

    for i in range(2, uptoNum+1):
        if number % i != 0:
            mutiplier = multiplyByWhat(number, i)
            number *= mutiplier

    return number
        
print(divisableByAllNumbers(uptoNum=20))
