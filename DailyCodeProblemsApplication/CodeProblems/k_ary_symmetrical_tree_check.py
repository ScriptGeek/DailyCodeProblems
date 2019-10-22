"""
Daily Interview Pro
Hi, here's your problem today. This problem was recently asked by Microsoft:

A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same as the right side of the tree.

Here's an example of a symmetrical k-ary tree.
        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9
Given a k-ary tree, figure out if the tree is symmetrical.

Here is a starting point:

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
  # Fill this in.

tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print is_symmetric(tree)
# True


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!

Daily Interview Pro
2019 Daily Interview Pro. All rights reserved.
Did this email bother you? Unsubscribe anytime.

# ScriptGeek's solution:

My solution traverses the k-ary tree using an iterative breadth-first-search 
algorithm. Each level of nodes gets tossed into an array to be analyzed to determine 
if the array values are symmetrical. Then if this check passes, toss each of these 
nodes' children in an array then loop back and repeat until all the nodes have been 
visited. If the code gets to the end without returning False then the tree is 
symmetrical, so it returns True.
"""

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
	stack = []
	nodes = []
	nodes.append(root)
	stack.append(nodes)
	while (len(stack) > 0):
		nodes = stack.pop()

		# Check for symmetry, return False on fail
		for i in range(0, len(nodes)//2):
			if (nodes[i].value != nodes[len(nodes) - 1 - i].value):
				return False
		childnodes = []
		for node in nodes:
			for childnode in node.children:
				childnodes.append(childnode)
		if (len(childnodes) > 0):
			  stack.append(childnodes)
			  
	return True 



# 1st test
tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print (is_symmetric(tree))
# True
	
# 2nd test
tree.children[1].children = [Node(1), Node(4), Node(8)]
print (is_symmetric(tree))
# False