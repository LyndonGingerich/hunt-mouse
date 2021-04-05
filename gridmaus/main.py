'''The game backend.
All addresses, including movement addresses, are tuples.
'''

import math
from random import random, sample


class World():
    '''Handles in-game abstractions'''
    def __init__(self, dimensions, size):
        self.dimensions = dimensions
        self.size = size

        dimension_center = int(self.size / 2)
        self.dimension_range = range(dimensions)

        self.goal = self.generate_goal()
        self.player_location = tuple(dimension_center for x in self.dimension_range)

    def generate_goal(self):
        '''Sets the goal at the beginning of the game'''
        return tuple(rand_range(self.size) for x in self.dimension_range)

    def move_address(self, address, movement):
        '''Helper function for World.move_player'''
        to_address = tuple(address[x] + movement[x] for x in self.dimension_range)
        return adjust_address_to_boundaries(to_address, self)

    def move_player(self, movement):
        '''Probably the most important method of the game'''
        self.player_location = self.move_address(self.player_location, movement)


def adjust_address_to_boundaries(address, world):
    '''Keeps the player from leaving the game area'''
    return tuple(adjust_coordinate_to_boundary(x, world.size - 1) for x in address)

def adjust_coordinate_to_boundary(coordinate, boundary):
    '''Helper function for adjust_address_to_boundary()
    Ensures that boundary <= coordinate <= 0.'''
    return boundary if coordinate > boundary else coordinate if coordinate >= 0 else 0

def eat_food():
    '''Victory message'''
    with open('gridmaus/foods.txt', 'r') as foods_file:
        foods = list(foods_file)
    food = sample(foods, 1)[0]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')

def get_distance(address1, address2):
    '''In Cartesian space using tuples
    Iterates by index to display correlation between address1[x] and address2[x]'''
    distances = tuple(abs(address1[x] - address2[x]) for x in range(len(address1)))
    return math.hypot(*distances)

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

def rand_range(maximum):
    '''Supposed to be faster than randrange'''
    return int(random() * maximum)

def run_game():
    '''The main game loop'''
    world_size = get_input('Length of game board: ', int)
    world_dimensions = get_input('Number of dimensions of game board: ', int)
    game_world = World(world_dimensions, world_size)
    coordinates_string = '\n'.join(tuple(
        f'Dimension {index}: {value}' for index, value in enumerate(game_world.player_location)
        ))
    velocity = 0

    while game_world.player_location != game_world.goal:
        print('Coordinates:', coordinates_string)
        print('Current velocity:', str(velocity))
        position1 = game_world.player_location
        move_template = None
        move_template = tuple(
            get_input(f'Movement in dimension {str(x)}: ', int) for x in game_world.dimension_range
            )
        game_world.move_player(tuple(move_template))
        position2 = game_world.player_location
        velocity = get_velocity(game_world.goal, position1, position2)

    eat_food()

    wishes_to_continue = input('Want to play again? (y/n)').lower()
    if wishes_to_continue in ('yes', 'y'):
        run_game()

if __name__ == '__main__':
    run_game()
