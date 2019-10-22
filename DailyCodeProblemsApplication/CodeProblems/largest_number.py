'''
Hi, here's your problem today. This problem was recently asked by Uber:

Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
def largestNum(nums):
  # Fill this in.

print largestNum([17, 7, 2, 45, 72])
# 77245217


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
'''

"""
ScriptGeek's solution:

It makes sense to use the numbers that begin with highest single digit first to build the largest
possible number from the given sequence of numbers.

So in order to arrange the numbers in a proper order the numbers have to be sorted in two ways.
The first sort needs to be done by length of the string in reverse order, so the numbers have to
be converted into strings. Before the sort an array has to be declared and the numbers parsed
into strings. After the first sort, the second sort needs to be performed by value.
By now the array of strings are properly sorted for the final step, which is popping the last 
string off the array until the array is empty. Each value popped off gets appended to the result.
When the array is empty the result is complete.

"""

def largestNum(nums):
    # convert all numbers to strings
    # sort the strings
    # build a string by popping the last string off the sorted list
    # return the string
    
    strings = []
    for num in nums:
        strings.append(str(num))

    # sort by length then by value
    strings.sort(key = lambda x:len(x), reverse=True)
    strings.sort(key = lambda x:x[0])

    result = ""
    while (len(strings)>0):
        result += strings.pop()

    return result



print(largestNum([17, 7, 2, 45, 72]))
# 77245217
