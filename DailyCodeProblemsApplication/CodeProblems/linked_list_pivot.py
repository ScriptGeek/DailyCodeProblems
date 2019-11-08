'''
This problem was asked by LinkedIn.

Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come 
before nodes greater than or equal to k.

For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
'''
class Link:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def append(self,link):
        newLink=link
        if self.head==None and self.tail==None:
            self.head=newLink
            self.tail=newLink
        else:
            self.tail.next=newLink
            self.tail=newLink
            self.count+=1
        newLink.next = None

    def pop(self,index):
        curr=self.head
        prev=self.head
        for i in range(0,index):
            prev=curr
            curr=curr.next
        if curr == self.tail:
            self.tail=prev
            self.tail.next=None
        if curr == self.head:
            self.head=curr.next
        else:
            prev.next = curr.next
        curr.next=None
        self.count-=1
        return curr

    def index(self,value):
        link=self.head
        while True:
            link=link.next
            if link==None | link.value==value:
                break
        return link

    def pivot(self, k):
        curr=self.head
        index=-1
        fst=None
        while fst!=curr:
            index+=1
            next=curr.next
            if (curr.value >= k):
                if fst==None:
                    fst=curr
                lnk=self.pop(index)
                index-=1
                self.append(lnk) # pop link and append to the end
            curr=next

    def print(self):
        curr=self.head
        if curr==None:
            print("Empty")
        else:
            lst = []
            while curr!=None:
                lst.append(curr.value)
                curr=curr.next
            print(' -> '.join(map(str,lst)))

lst=LinkList()
lst.append(Link(5))
lst.append(Link(1))
lst.append(Link(8))
lst.append(Link(0))
lst.append(Link(3))
lst.print()
lst.pivot(3)
lst.print()


