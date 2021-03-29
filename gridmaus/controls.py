'''Holds control stuff to keep it out of the way of the main file'''

class KeypadControls():
    '''For 2D manual mode for demonstration'''
    def __init__(self, world):
        self.world = world

    def moveDown(self):
        '''Numpad 2 or down arrow'''
        return self.keypadMove(1, -1)

    def moveDownLeft(self):
        '''Numpad 1'''
        return self.keypadMove(-1, -1)

    def moveDownRight(self):
        '''Numpad 3'''
        return self.keypadMove(1, -1)

    def moveLeft(self):
        '''Numpad 4 or left arrow'''
        return self.keypadMove(0, -1)

    def moveRight(self):
        '''Numpad 6 or right arrow'''
        return self.keypadMove(0, 1)

    def keypadMove(self, *movements):
        '''Translates for the move() function'''
        return self.world.movePlayer(movements)

    def moveUp(self):
        '''Numpad 8 or up arrow'''
        return self.keypadMove(1, 1)

    def moveUpLeft(self):
        '''Numpad 7'''
        return self.keypadMove(-1, 1)

    def moveUpRight(self):
        '''Numpad 9'''
        return self.keypadMove(1, 1)
