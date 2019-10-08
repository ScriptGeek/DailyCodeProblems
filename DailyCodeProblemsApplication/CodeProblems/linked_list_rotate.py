"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!
"""

'''
ScriptGeek's solution:

I created my own custom linked list data structure for use with this exercise.
It's a doubly linked list. Then I created a linked list and then a print method for testing.
Then I created the method for shifting the linked list, which was pretty trivial, as it just
does the obvious, messing with pointers to each link every which way.
'''


class Link:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def next(self):
        self.current = self.current.next
        return self.current

    def hasNext(self):
        return self.current.next != None



class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def appendLink(self, value):
        newLink = Link(value)
        if (self.tail == None):
            self.tail = newLink
            self.head = newLink
        else:
            self.tail.next = newLink
            newLink.prev = self.tail
            self.tail = newLink

    def prependLink(self, value):
        newLink = Link(value)
        if (self.head == None):
            self.head = newLink
            self.tail = newLink
        else:
            newLink.next = self.head
            self.head.prev = newLink
            self.head = newLink

    def shift(self, k):
        for n in range(0,k):
            self.head.prev = self.tail
            prevhead = self.head
            self.head = self.tail
            self.head.next = prevhead
            self.tail = self.head.prev
            self.tail.next = None
            self.head.prev = None

    def print(self):
        current = self.head
        while (True):
            print (current.value)
            current = current.next
            if (current == None):
                break


def runTest():
    linklist = LinkedList()
    linklist.appendLink(1)
    linklist.appendLink(2)
    linklist.appendLink(3)
    linklist.appendLink(4)
    linklist.appendLink(5)
    
    k = 3

    print("Links in LinkedList:")
    linklist.print()
    linklist.shift(k)
    print(f"shifted: {k}")
    linklist.print()
