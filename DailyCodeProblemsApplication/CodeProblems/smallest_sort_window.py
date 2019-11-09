'''
Hi, here's your problem today. This problem was recently asked by Twitter:
Given a list of numbers, find the smallest window to sort such that the whole list will be sorted.
If the list is already sorted return (0, 0). You can assume there will be no duplicate numbers.

Example:
Input: [2, 4, 7, 5, 6, 8, 9]
Output: (2, 4)
Explanation: Sorting the window (2, 4) which is [7, 5, 6] will also means that the whole list is sorted.

ScriptGeek's solution:

1. Create a sorted list of the given list
2. Compare the two lists, the first value that doesn't match is the first value in the range
The last value that doesn't match is the last value in the range
3. Return the tuple with the first and last values

'''
def min_window_to_sort(nums):
    print(nums)
    sorted_nums=sorted(nums)
    start=0
    end=0
    for i in range(0,len(nums)):
        if (sorted_nums[i]!=nums[i]):
            if start==0:
                start=i
            else:
                end=i
    return (start,end)

print(min_window_to_sort([2, 7, 3, 4, 5, 8, 9]))
# (2, 4)
