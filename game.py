"""The main game file, which you run to run the game."""

from random import choice, randrange
from shutil import get_terminal_size

import script
from helpers import *
from input import *

DIVIDER = '-' * get_terminal_size().columns
MOVEMENT_OPERATORS = {'+': 1, '-': -1, '': 0, '1': 1, '0': 0, '-1': -1}


class Game:
    """Handles in-game abstractions"""

    def __init__(self, dimensions, size):
        self.dimensions = dimensions
        self.size = size
        self.goal = tuple(randrange(self.size) for _ in range(self.dimensions))
        dimension_center = int(self.size / 2)
        self.player_location = repeat_tuple(dimension_center, self.dimensions)

    def move_player(self, velocity):
        """Where the action happens"""

        def move_manually():
            def get_operator_input(dimension):
                return validate_input_of_values(
                    message=f'Movement in dimension {dimension}: ',
                    valid_values=set(MOVEMENT_OPERATORS.keys())
                )

            print(DIVIDER)
            print('Coordinates:', self.player_location)
            print('Current velocity:', str(velocity))
            return tuple(map(get_operator_input, range(self.dimensions)))

        operators = move_manually() if script.PLAY_MANUALLY else script.move(velocity)
        movement = (MOVEMENT_OPERATORS[x] for x in operators)

        self.player_location = tuple(map(sum, zip(self.player_location, movement)))


def eat_food():
    """Victory message"""
    with open('foods.txt', 'r') as foods_file:
        foods = list(foods_file)
    food = choice(foods)
    food = food.rstrip('\n')
    print(f'You find and devour {food}. Victory is sweet.')


def get_game_details():
    """Defines the size and dimension of the game by user input"""

    def get_manual_game_details():
        """Uses get_int_input to get game details from the user"""

        def succinct_game_details():
            return (
                get_natural_input('How many units long would you like this game to be in each dimension? '),
                get_natural_input('In how many dimensions would you like to play? ')
            )

        return succinct_game_details()

    return get_manual_game_details() if script.PLAY_MANUALLY else (script.game_size, script.game_dimensions)


def run_game():
    """The main game loop.
    The tutorial is available when not playing by script."""

    def get_velocity(goal, from_address, to_address):
        return distance(from_address, goal) - distance(to_address, goal)

    # initialize
    game_size, game_dimensions = get_game_details()
    game = Game(game_dimensions, game_size)

    # play
    moves = Counter()
    velocity = 0
    to_position = game.player_location
    while to_position != game.goal:
        from_position = to_position
        game.move_player(velocity)
        to_position = game.player_location
        velocity = get_velocity(game.goal, from_position, to_position)
        moves.increment()

    # finish
    if script.PLAY_MANUALLY:
        eat_food()
    print(f'You won in only {moves.read()} moves!')


if __name__ == '__main__':
    run_game()
