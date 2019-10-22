"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the
two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

Upgrade to premium and get in-depth solutions to every problem, including this one.
Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here!
As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!

# ScriptGeek's solution:
Iterate through all the combos O(n^2) loop in list of strings
Don't check if both loops are at the same iteration value
Concatenate the two strings and check if they are palindromes
If palindrom is found add indices to a list
Display the list when complete

Interestingly, in the subject line of the email this problem was sent in it said it was Hard.
I found this problem to be less difficult than the fibonacci problem.
"""


def findPairs(list):
    results = []
    for n in range(0, len(list)):
        for m in range(0, len(list)):
            if (n != m):
                if (isPalindrome(list[n]+list[m])):
                    results.append(("("+str(n)+", "+str(m)+")"))
                    print (f"n: {n} m: {m}")

def isPalindrome(string):
    for n in range(0, len(str(string))//2):
        if (string[n] != string[len(string) - 1 - n]):
            return False
    return True


findPairs(["code", "edoc", "da", "d"])

