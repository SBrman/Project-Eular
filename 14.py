#! python3

"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import  time
import threading

start = time.time()

def collatz_length(n):
    length = 0
    while True:
        length += 1
        if n == 1:
            return length
        n = n//2 if n%2==0 else (3*n + 1)

def chain_range(lower, upper):    
    max_chain_length = 0
    for i in range(lower, upper):
        length = collatz_length(i)
        if length > max_chain_length:
            max_chain_length = length
            number = i
    numbers[number] = max_chain_length
    return (max_chain_length, number)

threads = []
numbers = {}

for i in range(1,1000001,10000):
    thread = threading.Thread(target=chain_range, args=[i, i+10000])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

startNum, chainLen = max(zip(numbers.values(), numbers.keys()))
print(f'Starting Number is {startNum} and Chain length is {chainLen}')
print(f'Time took: {time.time()-start} second.')


##def print_collatz(number):
##    seq = collatz(number)
##    numbers = [str(num) for num in seq]
##    text = ' -> '.join(numbers)
##    return text
##
##def collatz(n, list_of_num=None):
##    if n == 1:
##        if list_of_num == None:
##            return [1,]
##        return list_of_num
##
##    if list_of_num == None:
##        list_of_num = []
##    
##    n = n//2 if n%2==0 else (3*n + 1)
##    list_of_num.append(n)
##    list_of_num = collatz(n, list_of_num)
##    return list_of_num
##
##def largest_seq_under(limit):
##    max_chain_length = 1
##    for i in range(1, limit):
##        length = len(collatz(i))
##        if length > max_chain_length:
##            max_chain_length = length
##            number = i
##    return number, max_chain_length

##print(collatz_length(25))
##print(largest_seq_under(1000000))
##print(len(collatz(837799)))