'''Holds control stuff to keep it out of the way of the main file'''

import pygame_menu

import main

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

def run_move_menu(world, velocity=0):
    '''In-game display'''
    menu = pygame_menu.Menu(
        'Welcome',
        main.SCREEN_HEIGHT,
        main.SCREEN_WIDTH,
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
    menu.mainloop(main.screen)
