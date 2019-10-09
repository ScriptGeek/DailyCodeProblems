"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!
"""

'''
ScriptGeek's solution:

A function called roll takes a goal, which is an array of integers representing the set of die values needed to stop the cycle.
This function also takes an additional value for the number of sides in the die, for extra nerd points.

I predicted no difference between either game option, due to my theory that each side of the die has equal probability for each roll.

Running the test for 100000 samples (number of games played) these are the results for each batch of sampling:
average rolls for 1st game (5 then 6): 40.94087
average rolls for 2nd game (5 then 5): 40.78491

average rolls for 1st game (5 then 6): 41.04696
average rolls for 2nd game (5 then 5): 41.07448

average rolls for 1st game (5 then 6): 40.88335
average rolls for 2nd game (5 then 5): 41.0841

The results show an insignificant difference between the two games; therefore, there exists no advantage with either game option.

'''


import random

# rolls dice until the given goal has been reached for dice with the specified number of sides then returns the number of rolls
def roll(goal, sides):
    rolls = 0
    index = 0
    while (True):
        value = random.randint(1,sides)
        if (value == goal[index]):
            index += 1
            if (index == len(goal)):
                return rolls
        else:
            index = 0
        rolls += 1


def runTest():
    print ("runTest")

    sampleSize = 100000
    totalRolls = [0,0]

    for sample in range (0,sampleSize):
        totalRolls[0] += roll([5,6],6)
        totalRolls[1] += roll([5,5],6)
    
    print (f"average rolls for 1st game (5 then 6): {totalRolls[0]/sampleSize}")
    print (f"average rolls for 2nd game (5 then 5): {totalRolls[1]/sampleSize}")
