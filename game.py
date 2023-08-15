"""The main game file, which you run to run the game."""

from random import choice, randrange
from shutil import get_terminal_size

import script
from helpers import *
from input import *
from input import get_natural_input

DIVIDER = '-' * get_terminal_size().columns
MOVEMENT_OPERATORS = {'+': 1, '-': -1, '': 0, '1': 1, '0': 0, '-1': -1}


class Game:
    """Handles in-game abstractions"""

    def __init__(self):
        self.dimensions, self.size = (
            get_natural_input('Number of dimensions: '),
            get_natural_input('Game size in each dimension: ')
        ) if script.PLAY_MANUALLY else (
            script.game_size, script.game_dimensions
        )

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
            return tuple(get_operator_input(i) for i in range(self.dimensions))

        def get_new_player_coordinates():
            new_movement = move_manually() if script.PLAY_MANUALLY else script.move(velocity)
            for coordinate, operator in zip(self.player_location, new_movement):
                yield coordinate + MOVEMENT_OPERATORS[operator]

        self.player_location = tuple(get_new_player_coordinates())


def eat_food():
    """Victory message"""
    with open('foods.txt', 'r') as foods_file:
        foods = list(foods_file)
    food = choice(foods)
    food = food.rstrip('\n')
    print(f'You find and devour {food}. Victory is sweet.')


def run_game():
    """The main game loop.
    The tutorial is available when not playing by script."""

    # initialize
    game = Game()

    # play
    moves = Counter()
    velocity = 0
    current_distance = distance(game.player_location, game.goal)
    while game.player_location != game.goal:
        game.move_player(velocity)
        new_distance = distance(game.player_location, game.goal)
        velocity = current_distance - new_distance
        current_distance = new_distance
        moves.increment()

    # finish
    if script.PLAY_MANUALLY:
        eat_food()
    print(f'Number of moves: {moves.read()}')


if __name__ == '__main__':
    run_game()
