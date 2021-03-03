import navigation
import newworld

class Maus:
    def __init__(self, *coordinates):
        self.loc = list(coordinates)

worldDimensions = input('Number of dimensions: ')
worldLength = input('World size in cells: ')
world = newworld.newWorld(worldDimensions, worldLength)