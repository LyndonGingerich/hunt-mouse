'''The game backend
All addresses, including movement addresses, are tuples.'''

import json
import math
from random import choice, randrange

import script


class World:
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
        return tuple(randrange(self.size) for x in self.dimension_range)
    
    def get_movement(self, velocity):
        '''Retrieves movement data from the player'''
        if options['manual_play']:
            coordinates_string = '\n'.join(tuple(
                f'Dimension {index}: {value}' for index, value in enumerate(game_world.player_location)
                ))
            print('Coordinates:', coordinates_string)
            print('Current velocity:', str(velocity))
            movement = tuple(
                get_input(f'Movement in dimension {str(x)}: ', int) for x in game_world.dimension_range
                )
            return movement
        return script.move(velocity)

    def move_player(self, movement):
        '''Probably the most important method of the game'''
        current_address = self.player_location
        movement_address = tuple(current_address[x] + movement[x] for x in self.dimension_range)
        to_address = adjust_address_to_boundaries(movement_address, self.size - 1)
        if options['manual_play'] and to_address != movement_address:
            print('Pow! The mouse runs into a wall!')
        self.player_location = to_address


def adjust_address_to_boundaries(address, boundary):
    '''Keeps the player from leaving the game area'''
    return tuple(adjust_coordinate_to_boundary(x, boundary) for x in address)

def adjust_coordinate_to_boundary(coordinate, boundary):
    '''Helper function for adjust_address_to_boundary()
    Ensures that boundary <= coordinate <= 0.'''
    if coordinate > boundary:
        return boundary
    if coordinate < 0:
        return 0
    return coordinate

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

def get_options():
    with open('options.json', 'r') as options_file:
        options_JSON = options_file.read()
    options = json.loads(options_JSON)
    return options

def get_velocity(goal, from_address, to_address):
    '''The player gets a readout of this.'''
    return get_distance(from_address, goal) - get_distance(to_address, goal)

def get_world_details():
    '''Defines the size and dimension of the game world'''
    if options['manual_play']:
        size = get_input('Length of game world: ', int)
        dimensions = get_input('Number of dimensions of game world: ', int)
        return size, dimensions
    return script.size, script.dimensions


if __name__ == '__main__':
    while True:
        options = get_options()
        world_size, world_dimensions = get_world_details()
        game_world = World(world_dimensions, world_size)
        velocity = 0

        while game_world.player_location != game_world.goal:
            position1 = game_world.player_location
            game_world.move_player(game_world.get_movement(velocity))
            position2 = game_world.player_location
            velocity = get_velocity(game_world.goal, position1, position2)

        eat_food()

        wishes_to_continue = input('Want to play again? (y/n)').lower()
        if not wishes_to_continue in ('yes', 'y'):
            break
