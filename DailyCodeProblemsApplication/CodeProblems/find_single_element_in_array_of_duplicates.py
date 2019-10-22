"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.
Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7
class Solution(object):
  def findSingle(self, nums):
    # Fill this in.

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3


Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
"""

class Solution(object):
  def findSingle(self, nums):
    dict = {}
    for i in range(0, len(nums)):
        val = dict.setdefault(nums[i], 0)
        dict.update({nums[i]: val + 1})
    for key in dict.keys():   
        if (dict[key] == 1):
            return str(key)
    return "single not found"

nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
