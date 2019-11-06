'''
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

1. search for smallest digit (right to left) that can be swapped with the next largest digit to the right
1b. swap in
2. search for the lowest digit to the right
of the index of the digit that was swapped out
3. swap the lowest digit in
4. go back to step 2 until the remaining digits are compared
'''

def find_next_permutation(num):
    numstr = str(num)
    digits = len(numstr)
    swapme = 0
    lt = list(numstr)
    next_higher_index = lt.index(max(numstr))
    # search from 2nd to last
    nums = {}
    for c in range(-2, -digits, -1):
        # search for the next higher digit to the right
        for k in range(c+1, -1):
            if int(numstr[c]) < int(numstr[k]):
                # number to the right is bigger, remember this number for later
                nums.setdefault(c, k)

    # scrape from the dictionary the next bigger number and swap it out
    key_list = list(nums.keys())
    val_list = list(nums.values())
    next_higher_index = min(val_list)
    swapme = key_list[val_list.index(next_higher_index)]
    l = list(numstr)
    temp = l[swapme]
    l[swapme] = l[next_higher_index]
    l[next_higher_index] = temp

    # reorders the given list starting at start index to the lowest value
    def reorder_to_lowest(lst, start):
        temp=list(lst)
        result=[]
        for i in range(0-len(temp), start):
            result.append(temp.pop(0))
        while len(temp) > 0:
            m = min(temp)
            ind = temp.index(m)
            result.append(m)
            temp.pop(ind)
        return int(''.join(result))

    return reorder_to_lowest(l,swapme+1)

print(find_next_permutation(48975))
# 49578