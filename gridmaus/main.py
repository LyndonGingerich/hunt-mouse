'''The game backend, and also frontend.
All addresses, including movement addresses, are tuples.
'''

import math
from random import random
import pygame
import pygame_menu

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class BuildWorld():
    '''Isn't a world, but prepares to build one'''
    def __init__(self):
        self.dimensions = 2
        self.size = 5

    def change_size(self, _, size):
        '''Called by selector onchange'''
        self.size = size

    def change_dimensions(self, _, dimensions):
        '''Called by selector onchange'''
        self.dimensions = dimensions


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
        return tuple(rand_int(self.size) for x in self.dimension_range)

    def movePlayer(self, movement):
        '''Pretty much all the controls are hooked here.'''
        return tuple(
            adjust_to_boundaries(self.player_location[x] + movement[x], self.size - 1)
            for x in movement
            )


def adjust_to_boundaries(coordinate, boundary):
    '''Keeps the player from leaving the game area'''
    return boundary if coordinate > boundary else 0 if coordinate < 0 else coordinate

def eat_food():
    '''Victory message'''
    with open('foods.txt', 'r') as foods_file:
        foods = [foods_file]
    food = foods[rand_int(len(foods))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')

def game_loop():
    '''The main game loop'''
    game_world = World(build_world.dimensions, build_world.size)
    running = True
    while running:
        old_address = game_world.player_location
        game_world.player_location = game_world.movePlayer(
            tuple(rand_int(3) - 1 for x in game_world.dimension_range)
            )
        if old_address == game_world.player_location:
            running = False
        else:
            player_velocity = get_velocity(game_world.goal, old_address, game_world.player_location)
            print(player_velocity) # for testing; pipe to display

def generate_numerical_selector(min_size, max_size):
    '''Helper function for Game.showMenu()'''
    return [(str(x), x) for x in range(min_size, max_size + 1)]

def get_difference(int1, int2):
    '''To shorten an unwieldy list comprehension'''
    return abs(int1 - int2)

def get_distance(address1, address2):
    '''In Cartesian space using tuples'''
    distances = tuple(get_difference(address1[x], address2[x]) for x in range(len(address1)))
    totalDistance = math.hypot(*distances)
    return totalDistance

def get_velocity(goal, address1, address2):
    '''The player gets a readout of this.'''
    return get_distance(address2, goal) - get_distance(address1, goal)

def rand_int(maximum):
    '''Supposed to be faster than randrange'''
    return int(random() * maximum)

def run_game_menu():
    '''Allows manual selection of world size; world dimensions are set to 2.'''
    menu = pygame_menu.Menu(
        'Welcome',
        300,
        400,
        theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.selector(
        'World size:',
        generate_numerical_selector(3, 10),
        onchange=build_world.change_size # passes <option text>, <option value>
    )
    menu.add.selector(
        'Dimensions:',
        generate_numerical_selector(2, 5),
        onchange=build_world.change_dimensions # passes <option text>, <option value>
    )
    menu.add.button('Begin', game_loop)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

def run_move_menu(world, velocity=0):
    '''In-game display'''
    menu = pygame_menu.Menu(
        'Welcome',
        SCREEN_HEIGHT,
        SCREEN_WIDTH,
        theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.label('Velocity: ' + str(velocity))
    for i in world.dimension_range:
        menu.add.selector(
            'Dimension ' + str(i),
            [('Forward', 1), ('Still', 0), ('Back', -1)],
            onchange=None
        )
    menu.add.button('Go', None)
    menu.add.button('Quit', None)
    menu.mainloop(screen)

if __name__ == '__main__':
    # Prime game
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Set world attributes
        build_world = build_world()
        run_game_menu()

        # Win
        eat_food()
