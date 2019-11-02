'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.

Upgrade to premium and get in-depth solutions to every problem, including this one.
Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here!
As always, shoot us an email if there's anything we can help with!

Looking to switch to Product Management?
Check out Daily Product Prep for product interview problems every day!
'''

def is_palindrome(n):
  # Fill this in.
  reversed = 0
  orig = int(n)
  while n != 0:
    remainder = n%10
    reversed = reversed * 10 + remainder
    n //= 10
  return reversed == orig

print (is_palindrome(121))
# True
print (is_palindrome(888))
# True
print (is_palindrome(678))
# False
