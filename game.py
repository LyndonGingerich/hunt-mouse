'''The main game file, which you run to run the game.
run_game() runs demo mode by default.'''

from math import hypot
from os import get_terminal_size
from random import choice, randrange

import script


DIVIDER = '-' * get_terminal_size()[0]

class Game:
    '''Handles in-game abstractions'''
    def __init__(self, dimensions, size, demo):
        self.demo = demo
        self.dimensions = dimensions
        self.size = size

        dimension_center = int(self.size / 2)
        self.dimension_range = range(dimensions)

        self.goal = self.generate_goal()
        self.player_location = tuple(dimension_center for _ in self.dimension_range)

    def generate_goal(self):
        '''Sets the goal at the beginning of the game'''
        return tuple(randrange(self.size) for _ in self.dimension_range)

    def get_movement(self, velocity):
        '''Retrieves movement data from the player'''
        def demo_movement():
            print(DIVIDER)
            coordinates_string = self.player_location
            print('Coordinates:', coordinates_string)
            print('Current velocity:', str(velocity))
            return tuple(
                input(f'Movement in dimension {str(x)}: ') for x in self.dimension_range
                )

        movement = demo_movement() if self.demo else script.move(velocity)
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

def get_converted_input(message, conversion_function):
    '''Checks input type until correct'''
    input_value = None
    error_types = {int: ValueError, string_to_bool: KeyError}
    error_to_check = error_types[conversion_function]
    error_messages = {
        ValueError: f'Input must be a valid `{conversion_function}`.',
        # KeyError is currently used only by string_to_bool().
        KeyError: 'Please enter input that can be parsed as either "yes" or "no".'
    }
    return_types = {int: int, string_to_bool: bool}
    while not isinstance(input_value, return_types[conversion_function]):
        try:
            input_value = conversion_function(input(message))
        except error_to_check:
            print(error_messages[error_to_check])
    return input_value

def get_velocity(goal, from_address, to_address):
    '''The player gets a readout of this.'''
    return get_distance(from_address, goal) - get_distance(to_address, goal)

def get_game_details(demo):
    '''Defines the size and dimension of the game by user input'''
    def demo_game_details():
        '''Uses get_converted_input to get game details from the user'''
        def succinct_game_details():
            return (
                get_converted_input(
                    'How many units long would you like this game to be in each dimension? ', int
                ),
                get_converted_input('In how many dimensions would you like to play? ', int)
            )

        def tutorial_game_details():
            details = size, dimensions = 5, 3
            print(DIVIDER)
            with open('tutorial.txt', 'r') as tutorial_text:
                print(tutorial_text.read())
            print(f'We will set this first game to {dimensions} dimensions, each of length {size}.')
            print(DIVIDER)
            return details

        tutorial = get_converted_input('Would you like to play the tutorial? (y/n)', string_to_bool)
        return tutorial_game_details() if tutorial else succinct_game_details()

    return demo_game_details() if demo else (script.game_size, script.game_dimensions)

def run_game(demo=True):
    '''The main game loop
    The tutorial is available within demo mode.'''
    def play_and_get_moves():
        '''Runs the actual gameplay; returns the number of moves the player took'''
        velocity = 0
        moves = 0
        while game.player_location != game.goal:
            from_position = game.player_location
            game.move_player(game.get_movement(velocity))
            to_position = game.player_location
            velocity = get_velocity(game.goal, from_position, to_position)
            moves += 1
        return moves

    if demo:
        with open('intro.txt', 'r') as intro_text:
            print(DIVIDER)
            print(intro_text.read())
            print(DIVIDER)
    game_size, game_dimensions = get_game_details(demo)
    game = Game(game_dimensions, game_size, demo)
    moves = play_and_get_moves()
    if demo:
        eat_food()
    print(f'You won in only {moves} moves!')

def string_to_bool(input_string):
    '''Gets boolean input from the terminal'''
    values = {'y': True, 'yes': True, 'n': False, 'no': False, '': False}
    return values[input_string.lower()]

if __name__ == '__main__':
    run_game()
