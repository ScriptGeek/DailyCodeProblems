"""
Hi, here's your problem today. This problem was recently asked by Facebook:

Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:
Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2
Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4

Here's a starting point:

def jumpToEnd(nums):
  # Fill this in.

print jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4])
# 2
"""

class Node:
    def __init__(self, name, index, value):
        self.name = name
        self.index = index
        self.value = value
        self.children = []
        self.depth = 0
        self.parent = None


def clip(val, min_, max_):
    return min_ if val < min_ else max_ if val > max_ else val


def jumpToEnd(nums):
    node = Node("root", 0, nums[0])
    stack = []
    stack.append(node)
    minDepthToLastIndexPos = len(nums)
    while (len(stack) > 0):
        node = stack.pop()
        clamp_max = len(nums)
        clamp_min = node.index + 1
        
        fromIndex = min(clamp_max, max(clamp_min, node.index + 1))
        toIndex = min(clamp_max, max(clamp_min, node.index + 1 + node.value))
        
        if (node.index == len(nums) - 1):
            if (minDepthToLastIndexPos > node.depth):
                minDepthToLastIndexPos = node.depth

        parentNode = node                
        for i in range(fromIndex, toIndex):
            node = Node(str(nums[i]), i, nums[i])
            node.parent = parentNode
            node.depth = parentNode.depth + 1
            stack.append(node)

    return minDepthToLastIndexPos


def runTest():
    value = jumpToEnd([3,2,5,1,1,9,3,4])
    print (f"minimum number of jumps: {value}")

