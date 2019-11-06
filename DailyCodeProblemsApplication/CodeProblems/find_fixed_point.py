'''
Hi, here's your problem today. This problem was recently asked by Apple:

A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same. Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements, or return None if it doesn't exist.
'''

def find_fixed_point(nums):
    result = None
    for i in range(0, len(nums)):
        if nums[i] == i:
            result=i
            break
        # exit if value greater than list length
        if nums[i] > len(nums):
            break
    return result

print (find_fixed_point([-5, 1, 3, 4]))
# 1

'''
Can you do this in sublinear time?
Yes, if the list contains values greater than the length of the sorted list of distinct elements execution can exit early.

I found this problem to be very trivial, it took only a few minutes to solve.
'''
