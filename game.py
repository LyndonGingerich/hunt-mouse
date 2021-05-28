'''The main game file, which you run to run the game.
run_game() runs demo mode by default.'''

from contextlib import contextmanager
import curses
from math import hypot
from random import choice, randrange

import script


@contextmanager
class Curse:
    '''Context manager for curses text'''
    def __init__(self):
        pass

    def __enter__(self):
        screen = curses.initscr()
        return screen

    def __exit__(self, *_):
        curses.endwin()

class Game:
    '''Handles in-game abstractions'''
    def __init__(self, dimensions, size, demo):
        self.demo = demo
        self.dimensions = dimensions
        self.size = size

        dimension_center = int(self.size / 2)
        self.dimension_range = range(dimensions)

        self.goal = self.generate_goal()
        self.player_location = tuple(dimension_center for x in self.dimension_range)

    def generate_goal(self):
        '''Sets the goal at the beginning of the game'''
        return tuple(randrange(self.size) for x in self.dimension_range)

    def get_movement(self, velocity):
        '''Retrieves movement data from the player'''
        if self.demo:
            print('-----')
            coordinates_string = self.player_location
            print('Coordinates:', coordinates_string)
            print('Current velocity:', str(velocity))
            movement = tuple(
                input(f'Movement in dimension {str(x)}: ') for x in self.dimension_range
                )
        else:
            movement = script.move(velocity)
        return convert_movement_address(movement)

    def move_player(self, movement):
        '''Probably the most important method of the game'''
        current_address = self.player_location
        movement_address = tuple(current_address[x] + movement[x] for x in self.dimension_range)
        self.player_location = movement_address


def convert_movement_address(movement):
    '''Transforms an operator movement address into an addition movement address'''
    operations = {'+': 1, '-': -1, '': 0}
    return tuple(operations[i] for i in movement)

def eat_food():
    '''Victory message'''
    with open('foods.txt', 'r') as foods_file:
        foods = list(foods_file)
    food = choice(foods)
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')

def get_distance(address1, address2):
    '''In Cartesian space using tuples
    Iterates by index to display correlation between address1[x] and address2[x]'''
    distances = tuple(abs(address1[x] - address2[x]) for x in range(len(address1)))
    return hypot(*distances)

def get_input(message, input_type):
    '''Checks input type until correct'''
    input_value = None
    while not isinstance(input_value, input_type):
        try:
            input_value = input_type(input(message))
        except ValueError:
            print(f'Input must be a valid `{input_type}`.')
    return input_value

def get_velocity(goal, from_address, to_address):
    '''The player gets a readout of this.'''
    return get_distance(from_address, goal) - get_distance(to_address, goal)

def get_game_details(demo):
    '''Defines the size and dimension of the game'''
    if demo:
        print('You will be navigating using Cartesian coordinates along multiple axes.')
        print('Each number you input will be added to the coordinate of your current location.')
        print('A positive number moves you "forward" and a negative number "backward".')
        size = get_input('How many units long would you like this game to be? ', int)
        dimensions = get_input('In how many dimensions would you like to play? ', int)
        return size, dimensions
    return script.game_size, script.game_dimensions

def intro_game():
    '''Prints game introduction'''
    print('''His gesticulations cause his lab coat to flap as wildly as his unkempt hair,
bleached from frequent late nights.
The fluorescent lighting glares off his glasses as he cackles.
The whiskers on your pointy nose prickle and your tail twitches apprehensively.
"Soon, my minion, we will conquer the multiverse!
Your natural olfactory prowess has been genetically enhanced,
harnessing your natural aptitude to grant you the power of inter-reality foraging!
Only trust your instincts, and the larders of who-knows-what parallel universe are yours!
It is time for your navigational training to begin in the dimensional slipstream!"
He flips a switch and fades from your sight into utter darkness.
But somewhere--in the distance, or perhaps close by--beckons the alien fulfillment of an ancient craving.
You can feel it.
-----''')

def run_game(demo=True):
    '''The main game loop'''
    if demo:
        intro_game()
    game_size, game_dimensions = get_game_details(demo)
    game = Game(game_dimensions, game_size, demo)
    velocity = 0
    movements = 0

    while game.player_location != game.goal:
        position1 = game.player_location
        game.move_player(game.get_movement(velocity))
        position2 = game.player_location
        velocity = get_velocity(game.goal, position1, position2)
        movements += 1

    print(f'You won in only {movements} moves!')
    if demo:
        eat_food()

if __name__ == '__main__':
    run_game()
