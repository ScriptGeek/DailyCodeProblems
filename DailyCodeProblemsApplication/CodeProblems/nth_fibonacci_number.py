"""
Hi, here's your problem today. This problem was recently asked by Apple:

The Fibonacci sequence is the integer sequence defined by the recurrence relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words, the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence:
 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
 
Given a number n, print the n-th Fibonacci Number.
Examples:
Input: n = 3
Output: 2
 
Input: n = 7
Output: 13
Here's a starting point:
 
class Solution():
 def fibonacci(self, n):
   # fill this in.
 
n = 9
print(Solution().fibonacci(n))

output should be: 34
 
 
Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.
 
Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.
 
Have a great day!

Daily Interview Pro
"""
#� 2019 Daily Interview Pro. All rights reserved.

#Did this email bother you? Unsubscribe anytime.


class Solution():
  def fibonacci(self, n):
    result = 0
    first = 0
    next = 1
    if (n < 2):
        result = n
    else:
        for i in range(0, n-1):
            result = first + next
            first = next
            next = result

    return result


n = 9
print(Solution().fibonacci(n))

