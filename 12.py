#! python3

"""
Highly divisible triangular number
Problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?

"""

def factorsOf(number):
    step = 1 if number%2 == 0 else 2
    divisors = (n for n in range(1, int(number**0.5)+1, step))

    factors = set()
    for divisor in divisors:
        if number % divisor == 0:
            factors.add(divisor)
            factors.add(number//divisor)
    factors.add(number)
    
    return list(factors)

    
def nthTriangle(n):
    numbers_in_nth_triangle = [num for num in range(1,n+1)]
    nth_triangle_number = sum(numbers_in_nth_triangle)

    factors = factorsOf(nth_triangle_number)
    
    return nth_triangle_number, factors

def tnw_divisors_more_than(number):    
    n = 1
    while True:
        triangleNumber, factors = nthTriangle(n)
        if len(factors) >= number:
            break
        n += 1
    return sorted(factors)[-1]

print(tnw_divisors_more_than(500))
