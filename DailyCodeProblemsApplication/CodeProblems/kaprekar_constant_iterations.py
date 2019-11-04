'''
Daily Interview Pro
Hi, here's your problem today. This problem was recently asked by Facebook:

Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

This certain function is as follows:
- Order the number in ascending form and descending form to create 2 numbers.
- Pad the descending number with zeros until it is 4 digits in length.
- Subtract the ascending number from the descending number.
- Repeat.

Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant.

ScriptGeek's solution:

An inner function 'order_number' was used as a helper and to keep the code in the loop clean.
The order_number function orders the digits in the number according to the ascending boolean parameter.
The loop in the num_kaprekar_iterations method calles the inner function twice for each iteration.
The result of the calculations is stored and used to create new numbers from the inner function.
The iterations variable stores the number of times the loop executes.
The value in the iterations variable is returned.
'''

KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):

    # Orders the given number num with respect to ascending value
    # NOTE: fails if num is a negative integer
    def order_number(num, ascending):
        numstr = str(num)
        numstr = '0' * (4-len(numstr)) + numstr  # ensure the number is 4 digits
        l = sorted(list(numstr))    # sort the digits in the number using a list
        if not ascending:
            l.reverse()
        numstr = ''.join(l)         # convert the list to a string
        return int(numstr)          # return the string converted to an int
    
    result = n
    iterations = 0
    while result != KAPREKAR_CONSTANT:
        iterations += 1
        # Get the ascending and descending numbers of the given number n
        ascending = order_number(result, True)
        descending = order_number(result, False)
        result = descending - ascending
    return iterations


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)

'''



'''
