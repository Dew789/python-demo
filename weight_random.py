'''
Two ways to accomplish weight random in python
'''

import random
from bisect import bisect


def histogram(s):
    '''Makes a histogram that contains the item from sequence

    s: lsit, tuple ,string
    
    returns: dict, map from each word to the number of times it appears
    '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def list_method(hist):
    '''Return random item bease on the weight, this method turn 
    hist into list accordance the times it appears then choose a random item

    hist: a dictionary of item and item's weights

    returns: value in dist's key
    '''
    t = [] 
    for value, weight in hist.items():       
        t.extend([value] * weight)
       
    return random.choice(t)
   
def iter_method(hist):
    '''Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.

    returns: value in dist's key
    '''
    values = []
    weights = []
    total_wigt = 0

    # make a list of values and a list of cumulative frequencies
    for value, weight in hist.items():
        total_wigt += weight
        values.append(value)
        weights.append(total_wigt)

    # choose a random value and find its location in the cumulation list
    rand = random.randint(0, total_wigt-1)
    index = bisect(weights, rand)
    return values[index]
