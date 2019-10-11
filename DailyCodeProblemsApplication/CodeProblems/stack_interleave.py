"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue.This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!
"""


def stack_interleave(stack):
    q = []
    count = 1 # start at 1st value in stack
    while(count < len(stack)):
        temp = stack.pop()
        subcount = len(stack)
        while(subcount > count):
            subcount -= 1
            q.append(stack.pop())
        stack.append(temp)
        while(len(q)>0):
            stack.append(q.pop(0))
        count += 1
    return stack


def runTest():
    print(f"[1,2,3,4,5]: {stack_interleave([1,2,3,4,5])}")
    print(f"[1,2,3,4]: {stack_interleave([1,2,3,4])}")