"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
Here's a starting point:

class Solution(object):
  def compress(self, chars):
    # Fill this in.

print Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
# ['a', '2', 'b', 'c', '3']


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
"""

"""
ScriptGeek's solution:
Loops through the array of characters, counts repeating characters, when a different character
is encountered, store the count of repeating characters and store the different character.
If reached the end of the loop with a repeated string, store the count.
Return the result.

Easy peasy
"""



class Solution(object):
    def compress(self, chars):
        result = [chars[0]]
        run = 1
        for i in range(1, len(chars)):
            if (chars[i]==chars[i-1]):
                run += 1
                if (i==len(chars)-1):
                    result.append(str(run))
            else:
                if (run > 1):
                    result.append(str(run))
                run = 1
                result.append(chars[i])

        return result


result = Solution().compress(['a', 'a', 'b', 'c', 'c', 'c'])
print (f"{result}")
# ['a', '2', 'b', 'c', '3']