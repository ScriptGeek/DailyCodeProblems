'''
Hi, here's your problem today. This problem was recently asked by Amazon:

The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar. The definition of the h-index is if a scholar has at least h of their papers cited h times.

Given a list of publications of the number of citations a scholar has, find their h-index.

Example:
Input: [3, 5, 0, 1, 3]
Output: 3
Explanation:
There are 3 publications with 3 or more citations, hence the h-index is 3.

Here's a starting point:

def hIndex(publications):
  # Fill this in.

print hIndex([5, 3, 3, 1, 0])
# 3
'''

'''
ScriptGeek's solution:

Consolidate the values in the array into a dictionary called citation_count_dict.
Use the value of each array indice as key.
Count the number of times each value appears in the array and store this as the value.
This dictionary maps the number of citations to the count of publications with the key
as number of citations.  Example: {5:1,3:2,1:1,0:1}

Create a dictionary and call it pre_h_index_dict.
    Key will be = publications with citation count >= value: Value = ??? (fill in later)

Get a list of keys in citation_count_dict, sort it, and iterate through this list
(call it citation_count_keys). eg: [0,1,3,5]
For each item in the list (citation_count_keys), iterate to the end of the list (inner loop),
count each value stored in citation_count_dict using the inner loop list value as key,
and store the result in pre_h_index_dict.

pre_h_index_dict should then look like: {0:5}, {1:4}, {3:3}, {5:1}
The value to return will be within pre_h_index_dict where the key will contain the highest value
where its value meets or exceeds its value in its dictionary entry.

This problem was actually fairly challenging to solve.
'''

def hIndex(publications):
    citation_count_dict = {}
    for i in range(0, len(publications)):
        v = citation_count_dict.setdefault(publications[i], 0) + 1
        citation_count_dict.update({publications[i]:v})
    pre_h_index_dict = {}
    citation_count_keys = sorted(citation_count_dict.keys())
    for i in range(0, len(citation_count_keys)):
        count = 0
        for j in range (i, len(citation_count_keys)):
            count += citation_count_dict[citation_count_keys[j]]
        pre_h_index_dict.setdefault(citation_count_keys[i], count)
    pre_h_index_dict_keys = sorted(pre_h_index_dict.keys())
    h_index = 0
    for i in range(0, len(pre_h_index_dict_keys)):
        if (pre_h_index_dict[pre_h_index_dict_keys[i]] >= pre_h_index_dict_keys[i]):
            h_index = pre_h_index_dict_keys[i]
    return h_index

def runTest():
    print (hIndex([5, 3, 3, 1, 0]))

