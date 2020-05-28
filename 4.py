#! python3

"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPalindrome(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[-(i+1)]:
            return False
    return True

largestNumber = 0
for num1 in range(999, 100, -1):
    for num2 in range(999, 100, -1):
        number = num1 * num2
        if isPalindrome(number):
            if number > largestNumber:
                largestNumber = number
                number_1, number_2 = num1, num2
            
print(largestNumber, ' = ', number_1, ' * ', number_2)
