#! python3

"""

Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,
5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of
3 or 5 below 1000.

"""

def allTheNumbers(belowNum):
    numbers = []
    for number in range(1, belowNum):
        if number % 3 == 0 and number % 5 == 0:
            numbers.append(number)
        elif number % 3 == 0:
            numbers.append(number)
        elif number % 5 == 0:
            numbers.append(number)
    return numbers

numbers = allTheNumbers(1000)
print(sum(numbers))
