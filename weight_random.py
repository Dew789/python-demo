'''
Two ways to accomplish weight random in python
'''

import random


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
    '''Return a random item bease on the weight in hist, this method turn 
    hist into list accordance the times it appears then choose a random item
    in list 

    hist: a dictionary of item and item's weights

    returns: value in dist's key
    '''
    data = [] 
    for value, weight in hist.items():       
        temp = [value] * weight
        data.extend(temp)
       
    rand = random.randint(0,len(all_data)-1) 
    return data[rand]
   
def iter_method(hist):
    '''Return a random item bease on the weight in hist, this method
    adds weight one by one till the total bigger than the random number 

    hist: a dictionary of item and item's weights

    returns: value in dist's key
    '''
    total = sum(hist.values()) 
    rand = random.randint(1,total)
      
    cur_total = 0
    for value, weight in hist.items(): 
        cur_total += weight
        if rand <= cur_total:
            return value