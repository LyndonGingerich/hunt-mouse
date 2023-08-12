"""The main game file, which you run to run the game.
run_game() runs demo mode by default."""

from shutil import get_terminal_size
from random import choice, randrange

from helpers import *
from input import *
import script

DIVIDER = '-' * get_terminal_size().columns
MOVEMENT_OPERATORS = {'+': 1, '-': -1, '': 0, '1': 1, '0': 0, '-1': -1}


class Game:
    """Handles in-game abstractions"""

    def __init__(self, dimensions, size, demo):
        self.demo = demo
        self.dimensions = dimensions
        self.size = size
        self.goal = tuple(randrange(self.size) for _ in range(self.dimensions))
        dimension_center = int(self.size / 2)
        self.player_location = repeat_tuple(dimension_center, self.dimensions)

    def get_movement(self, velocity):
        """Retrieves movement data from the player"""

        def demo_movement():
            def get_operator_input(dimension):
                return validate_input_of_values(
                    message=f'Movement in dimension {dimension}: ',
                    valid_values=set(MOVEMENT_OPERATORS.keys())
                )

            print(DIVIDER)
            print('Coordinates:', self.player_location)
            print('Current velocity:', str(velocity))
            return map(get_operator_input, range(self.dimensions))

        movement = demo_movement() if self.demo else script.move(velocity)
        return (MOVEMENT_OPERATORS[x] for x in movement)

    def move_player(self, movement):
        """Where the action happens"""
        self.player_location = tuple(map(sum, zip(self.player_location, movement)))


def eat_food():
    """Victory message"""
    with open('foods.txt', 'r') as foods_file:
        foods = list(foods_file)
    food = choice(foods)
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')


def get_game_details(demo):
    """Defines the size and dimension of the game by user input"""

    def demo_game_details():
        """Uses get_int_input to get game details from the user"""

        def succinct_game_details():
            return (
                get_natural_input('How many units long would you like this game to be in each dimension? '),
                get_natural_input('In how many dimensions would you like to play? ')
            )

        def tutorial_game_details():
            details = size, dimensions = 5, 3
            print(DIVIDER)
            with open('tutorial.txt', 'r') as tutorial_text:
                print(tutorial_text.read())
            print(f'We will set this first game to {dimensions} dimensions, each of length {size}.')
            return details

        tutorial = get_bool_input('Would you like to play the tutorial? (y/n)')
        return tutorial_game_details() if tutorial else succinct_game_details()

    return demo_game_details() if demo else (script.game_size, script.game_dimensions)


def run_game(demo=True):
    """The main game loop
    The tutorial is available within demo mode."""

    def get_velocity(goal, from_address, to_address):
        return distance(from_address, goal) - distance(to_address, goal)

    def play_and_get_moves():
        """Runs the actual gameplay; returns the number of moves the player took"""
        velocity = cumulative_moves = 0
        to_position = game.player_location
        while tuple(to_position) != game.goal:
            from_position = to_position
            game.move_player(game.get_movement(velocity))
            to_position = game.player_location
            velocity = get_velocity(game.goal, from_position, to_position)
            cumulative_moves += 1
        return cumulative_moves

    if demo:
        with open('intro.txt', 'r') as intro_text:
            print(DIVIDER, intro_text.read(), DIVIDER, sep='\n')
    game_size, game_dimensions = get_game_details(demo)
    game = Game(game_dimensions, game_size, demo)
    moves = play_and_get_moves()
    if demo:
        eat_food()
    print(f'You won in only {moves} moves!')


if __name__ == '__main__':
    run_game()
