'''The game controls.
This file calls backend.py.'''

import sys

import pygame
import pygame_menu

sys.path.append('..')

from gridmaus.gridmaus import backend

MENU_HEIGHT = 400
MENU_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 600


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


def run_game():
    '''The main game loop'''

    def edit_move_template(_, index, value):
        '''Called by show_move_menu()'''
        move_template[index] += value

    def show_move_menu(world, velocity):
        '''In-game display'''
        menu = pygame_menu.Menu(
            'Velocity: ' + str(velocity),
            MENU_WIDTH,
            MENU_HEIGHT,
            theme=pygame_menu.themes.THEME_BLUE
        )
        for i in world.dimension_range:
            menu.add.selector(
                'Dimension ' + str(i),
                [('Forward', i, 1), ('Still', i, 0), ('Back', i, -1)],
                onchange=edit_move_template
            )
        menu.add.button('Go', pygame_menu.events.CLOSE)
        menu.add.button('New game', pygame_menu.events.RESET)
        menu.mainloop(screen)

    game_world = backend.create_world()
    move_template = [0 for x in game_world.dimension_range]
    velocity = 0
    while game_world.player_location != game_world.goal:
        show_move_menu(game_world, velocity)
        velocity = game_world.move_player(tuple(move_template))

def show_main_menu():
    '''Allows manual selection of world size and dimensions.'''
    menu = pygame_menu.Menu(
        'Welcome',
        MENU_WIDTH,
        MENU_HEIGHT,
        theme=pygame_menu.themes.THEME_BLUE
    )
    menu.add.selector(
        'Game size:',
        backend.generate_numerical_selector(
            backend.MIN_SIZE,
            backend.MAX_SIZE,
            'size'
        ),
        default=backend.world_template['size'] - backend.MIN_SIZE,
        onchange=backend.change_world_template # passes <option text>, <option value>
    )
    menu.add.selector(
        'Dimensions:',
        backend.generate_numerical_selector(
            backend.MIN_DIMENSIONS,
            backend.MAX_DIMENSIONS,
            'dimensions'
        ),
        default=backend.world_template['dimensions'] - backend.MIN_DIMENSIONS,
        onchange=backend.change_world_template # passes <option text>, <option value>
    )
    menu.add.button('Begin', run_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    show_main_menu()
