'''Modify this file, especially move(), to play Gridmaus by script.'''

from random import randrange # needed only for sample code

game_dimensions = 3
game_size = 5

def move(velocity):
    '''The function run by the game to get new movements
    Movements are iterables of integers whose length equals world_length.'''
    return [randrange(3) - 1 for x in range(game_dimensions)]
