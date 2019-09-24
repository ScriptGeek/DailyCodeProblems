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

# ScriptGeek's solution:

"""
My solution uses an n-ary tree. The input array of values is used to generate this tree.
Each relationship between index positions within the array is represented in the tree.
After all relationships are created the determination is complete.
At each point where the node for the last index position is created a depth comparison
is made. The depth of the node is the same as the number of jumps. If the depth of the
node is lesser than the previously determined depth, then this value becomes the new
depth. When all the nodes are created the depth is returned.
"""

# class used for building an n-ary tree data structure
class Node:
    def __init__(self, name, index, value):
        self.name = name
        self.index = index
        self.value = value
        self.children = []
        self.depth = 0
        self.parent = None

# calculates all possible pathways which can be taken to get the 1st element jumped
# over to the last element position and returns the least number of jumps.
def jumpToEnd(nums):

    # create the root node and push it to the stack
    node = Node("root", 0, nums[0])
    stack = []
    stack.append(node)
    minDepthToLastIndexPos = len(nums)

    # iterate until there are no more nodes in the stack
    while (len(stack) > 0):
        node = stack.pop()
        clamp_max = len(nums)
        clamp_min = node.index + 1
        
        # clamp the index positions to the input array size
        fromIndex = min(clamp_max, max(clamp_min, node.index + 1))
        toIndex = min(clamp_max, max(clamp_min, node.index + 1 + node.value))
        
        # if node is for last position and the depth is lesser, remember this depth
        if (node.index == len(nums) - 1):
            if (minDepthToLastIndexPos > node.depth):
                minDepthToLastIndexPos = node.depth

        # remember this node as the parent node
        parentNode = node

        # add all the children
        for i in range(fromIndex, toIndex):
            node = Node(str(nums[i]), i, nums[i])
            node.parent = parentNode
            node.depth = parentNode.depth + 1
            stack.append(node)

    return minDepthToLastIndexPos

# test this solution
def runTest():
    value = jumpToEnd([3,2,5,1,1,9,3,4])
    print (f"minimum number of jumps: {value}")

