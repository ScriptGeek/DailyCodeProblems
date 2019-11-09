"""
This problem was recently asked by Twitter:

Given a tree, find if the binary tree is height balanced or not. 
A height balanced binary tree is a tree where every node's 2 subtree do 
not differ in height by more than 1.


ScriptGeek's solution:

Traverse the tree in BFS (Breadth-First-Search) order.
Set a flag when finding a node with at least one missing child while traversing each level.
At the end of each level pass, if the missing child flag is set, then the level number is stored in a list.
After traversing the entire tree return 

The number of levels with missing children can be a maximum of only 2, due to the requirement of 
a height difference of 1. This is because any leaf nodes will have missing children and with a 
height difference of 1, there can be only 2 levels with missing children.

NOTE: There is a special case that needs consideration where the difference between levels is more than 1 even 
when the number of levels is only 2. To resolve this a calculation between the difference of these two levels 
is needed.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_height_balanced(tree):
    stack=[[tree]]
    incomplete_levels=0
    partial_levels_list=[]
    current_level=0
    while len(stack)>0:
        current_level+=1
        level=stack.pop()
        next_level=[]
        is_missing_child=False
        for node in level:
            if node.left!=None:
                next_level.append(node.left)
            if node.right!=None:
                next_level.append(node.right)
            if node.left==None or node.right==None:
                is_missing_child=True
        if is_missing_child:
            partial_levels_list.append(current_level)
        if len(next_level)>0:
            stack.append(next_level)
    if len(partial_levels_list) == 2:
        if abs(partial_levels_list[0]-partial_levels_list[1])<=1:
            return True
        else:
            return False
    else:
        return False

#     1
#    / \
#   2   3
#  / 
# 4   
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    /
#   2  
#  /
# 4 
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
