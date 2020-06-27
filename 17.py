#! python3

"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""
# 1st way
numbers = {  1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 
            90: 'Ninety', 0: ''}

def n2w(number):
    if 100 <= number < 1000:
        # divmod (x, y) returns (x//y, x%y)
        digits = divmod(number, 100)
        words = numbers[digits[0]] + ' hundred'
        if digits[1] != 0:
            return words + ' and ' + n2w(digits[1])
        else:
            return words
    elif 0 < number < 21:
        return numbers[number]
    elif 20 < number < 100:
        digits = divmod(number, 10)
        return numbers[number - digits[1]] + ' ' + numbers[digits[1]]
    elif number == 1000:
        return 'One Thousand'
    elif number == 0:
        return 'Zero'

letter_length = (len(n2w(i).replace(' ', '')) for i in range(1, 1001))
print(sum(letter_length))


# 2nd way
from num2words import num2words

length = (len(num2words(i).replace(' ','').replace(',','').replace('-','')) for i in range(1, 1001))
print(sum(length))
