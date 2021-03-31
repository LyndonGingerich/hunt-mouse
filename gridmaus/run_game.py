'''The game controls.
This file calls backend.py.'''

import sys

import pygame
import pygame_menu

sys.path.append('..')

from gridmaus.gridmaus import backend

# TODO: Add move menu "quit" code
# TODO: Add move menu "go" code
# TODO: Check game menu with knowledge of onreturn arguments

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class KeypadControls():
    '''For 2D manual mode for demonstration'''
    def __init__(self, world):
        self.world = world

    def move_down(self):
        '''Numpad 2 or down arrow'''
        return self.keypad_move(1, -1)

    def move_down_left(self):
        '''Numpad 1'''
        return self.keypad_move(-1, -1)

    def move_down_right(self):
        '''Numpad 3'''
        return self.keypad_move(1, -1)

    def move_left(self):
        '''Numpad 4 or left arrow'''
        return self.keypad_move(0, -1)

    def move_right(self):
        '''Numpad 6 or right arrow'''
        return self.keypad_move(0, 1)

    def keypad_move(self, *movements):
        '''Translates for the move() function'''
        return self.world.move_player(movements)

    def move_up(self):
        '''Numpad 8 or up arrow'''
        return self.keypad_move(1, 1)

    def move_up_left(self):
        '''Numpad 7'''
        return self.keypad_move(-1, 1)

    def move_up_right(self):
        '''Numpad 9'''
        return self.keypad_move(1, 1)


def iterate_game_loop(game_world):
    '''Iterate the game loop once'''

    move_template = [0 for x in game_world.dimension_range]

    def edit_move_template(index, value):
        '''Called by show_move_menu()'''
        move_template[index] += value

    def show_move_menu(world, velocity=0):
        '''In-game display'''
        menu = pygame_menu.Menu(
            'Velocity: ' + str(velocity),
            SCREEN_HEIGHT,
            SCREEN_WIDTH,
            theme=pygame_menu.themes.THEME_BLUE
        )
        for i in world.dimension_range:
            menu.add.selector(
                'Dimension ' + str(i),
                [('Forward', i, 1), ('Still', i, 0), ('Back', i, -1)],
                onchange=edit_move_template
            )
        menu.add.button('Go', None)
        menu.add.button('Quit', None)
        menu.mainloop(screen)

    show_move_menu(game_world)
    movement = tuple(move_template)
    move_results = game_world.move_player(movement)
    if move_results['reached_goal']:
        return False
    return move_results['velocity']

def run_game():
    '''The main game loop'''
    game_world = backend.create_world()
    current_velocity = True
    while current_velocity:
        current_velocity = iterate_game_loop(game_world)

def show_game_menu():
    '''Allows manual selection of world size and dimensions.'''
    menu = pygame_menu.Menu(
        'Welcome',
        300,
        400,
        theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.selector(
        'World size:',
        backend.generate_numerical_selector(3, 10),
        default=str(backend.world_template['size']),
        onchange=backend.change_world_template_size # passes <option text>, <option value>
    )
    menu.add.selector(
        'Dimensions:',
        backend.generate_numerical_selector(2, 5),
        default=str(backend.world_template['dimensions']),
        onchange=backend.change_world_template_dimensions # passes <option text>, <option value>
    )
    menu.add.button('Begin', run_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

pygame.init()

while True:
    show_game_menu()
