"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Given the root of a binary tree, print its level-order traversal. For example:

  1
 / \
2   3
   / \
  4   5

The following tree should output 1, 2, 3, 4, 5.

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_level_order(root):
  # Fill this in.

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
"""


'''
ScriptGeek's solution:

Start with the root node, push it onto a stack. Actually, this root node will be placed in an array and then
the array will be pushed onto a stack. The array represents all the nodes on the same level. The root node
is lonely all by itself on its level so it is the only one that goes into the array.

So while the stack has a level within, pop the level off the stack and iterate through its contents (nodes). 
Append the value of each node to a string. If each node has a child place the child in an array. After the 
iterative loop, if the array has any nodes within, push this array onto the stack. Repeat until the stack 
is empty.
'''


class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def print_level_order(root):
    s = []
    s.append([root])
    output = ""
    while (len(s) > 0):
        level = s.pop()
        nextlevel = []
        for n in level:
            output += str(n.val) + " "
            if (n.left != None):
                nextlevel.append(n.left)
            if (n.right != None):
                nextlevel.append(n.right)
        if (len(nextlevel) > 0):
            s.append(nextlevel)
    print (output)


root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
