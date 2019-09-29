"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?

Upgrade to premium and get in-depth solutions to every problem, including this one.
Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here!
As always, shoot us an email if there's anything we can help with!
"""

"""
ScriptGeek's solution:

I went for the gold and solved this problem without using any extra space. A single temporary
value stores an initial value to be swapped out and chains the swapping around the matrix
until the last swap where the temp variable value is assigned.

"""


def rotateMatrix90DegreesClockwise(mat):
    n = len(mat)
    for y in range(0, n//2):
        for x in range(0, (n+1)//2):
            temp = mat[y][x]
            mat[y][x] = mat[n-x-1][y]
            mat[n-x-1][y] = mat[n-y-1][n-x-1]
            mat[n-y-1][n-x-1] = mat[x][n-y-1]
            mat[x][n-y-1] = temp
    return mat


def runTest():

    # size of matrix
    n = 4

    # build a test matrix with n*n dimensions
    mat = []
    val = 1
    for y in range(0, n):
        mat.append([])
        for x in range(0,n):
            mat[y].append(val)
            val += 1

    # display matrix before rotation
    print(f"matrix before rotation: {mat}")

    mat = rotateMatrix90DegreesClockwise(mat)

    # display matrix after rotation        
    print(f"matrix after rotation: {mat}")
