"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
  # Fill this in.

print longest_run(242)
# 4


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
"""

def longest_run(n):
    b = bin(n)
    bstr=str(b)
    i = bstr.index("b") + 1
    runCount = 0
    longest = 0
    for c in bstr[i::]:
        if c != '1':
            if runCount > longest:
                longest = runCount
            runCount = 0
        else:
            runCount += 1
    return longest

print(longest_run(242))
