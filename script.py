'''Modify this file to play Gridmaus by script.'''

from random import randrange # needed only for sample code

dimensions = 3
size = 5 # length of each dimension

def move(velocity):
    return [randrange(size)] * dimensions