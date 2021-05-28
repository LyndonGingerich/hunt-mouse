'''Modify this file, especially move(), to play Gridmaus by script.'''

from collections import namedtuple
from random import choice # needed only for sample code

game_dimensions = 3
game_size = 5

Log = namedtuple('Log', ['movement', 'velocity'])
logs = []

def move(velocity):
    '''The function run by the game to get new movements
    Return an iterable of length game_size of values from possible_values.'''
    possible_values = ('+', '-', '')
    movement = [choice(possible_values) for _ in range(game_dimensions)] # definitely edit this
    logs.append(Log(movement, velocity))
    return movement
