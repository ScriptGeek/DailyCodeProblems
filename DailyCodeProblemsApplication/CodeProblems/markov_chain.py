"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

Upgrade to premium and get in-depth solutions to every problem, including this one. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

Ready to interview? Take Triplebyte's quiz and skip straight to final interviews with top tech companies!

No more? Unsubscribe.
"""


'''
ScriptGeek's solution:

So, the tuples (defined in the tp variable) are added to a dictionary. The dictionary is then 
used to store the probabilities for the various transitions. A loop is performed for the number 
of steps that will be taken. 

They said this was Easy. Well, it wasn't very difficult. I learned a little bit more about 
Python, so I accomplished both goals of learning Python and practicing programming concepts 
in this one.
'''


import random


def runTest():
    state = 'a'
    steps = 5000
    tp=[
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
        ]
    
    d={}
    for t in tp:
        if (not t in d):
            d.setdefault(t[0],{})
        d[t[0]].update({t[1]:t[2]})

    step = 0
    results = {}
    while (step < steps):
        r=random.choices(list(d[state].keys()), list(d[state].values()))
        v=results.setdefault(r[0],1)
        results.update({r[0]:v+1})
        step += 1

    print(results)
