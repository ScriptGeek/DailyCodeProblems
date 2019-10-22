"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!
"""


def find_greatest_common_denominator(values):
    
    smallest = min(values)
    gcd_found = False
    result = smallest

    while not gcd_found:
        for value in values:
            eval = value % smallest
            if (eval != 0):
                smallest -= 1
            else:
                gcd_found = True
                result = smallest
                break
            print (eval)


values = [42,56,14]

find_greatest_common_denominator(values)
