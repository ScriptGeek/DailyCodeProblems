"""
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

def longest_consecutive(nums):
  # Fill this in.

print longest_consecutive([100, 4, 200, 1, 3, 2])
# 4

Can you do this in linear time?

Upgrade to PRO and get in-depth solutions to every problem from ex-Google and ex-Facebook engineers TechLead and Joma.

Ready to fast-track your career? Join our premiere tech interview training program techinterviewpro.com.
If you liked this problem, let your friends know at dailyinterviewpro.com.

Have a great day!
"""

def longest_consecutive(nums):
	longest = 0
	nums.sort()
	last_num = nums[0]
	count = 1
	for n in range(1,len(nums)):
		if (nums[n] - last_num == 1):
			count += 1
			if (count > longest):
				longest = count
		else:
			count = 1
		last_num = nums[n]
	return longest

print( longest_consecutive([100, 4, 200, 1, 3, 2]) )
# 4


