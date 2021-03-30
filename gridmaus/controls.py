'''Holds control stuff to keep it out of the way of the main file'''

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
