"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""

# ScriptGeek's solution:
"""
I solved this problem by using two loops. The outer loop iterates through the input array.
The inner loop iterates through the input array as well, but it starts from the index 
position represented by the outer loop's current value. A comparison is made at each 
inner loop iteration with the value in the outer loop. If the value in the inner loop 
is smaller than the value in the outer loop, a variable is incremented. At the end of 
the inner loop this value is added to the result array. At the end of the outer loop 
the result array is returned.

This was a pretty trivial problem to solve, though. It was probably designed as a 
confidence booster for interviews.
"""


def smaller_to_the_right(values):
    result = []
    for i in range(0,len(values)):
        count = 0
        for n in range(i + 1,len(values)):
            if (values[i] > values[n]):
                count += 1
        result.append(count)
    return result

# test this solution

values = [3,4,9,6,1];
result = smaller_to_the_right(values);
print ("Input:")
print (str(values)[1:-1])
print ("Output:")
print (str(result)[1:-1])
