'''The game backend, and also frontend.'''

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

    def changeSize(self, _, size):
        '''Called by selector onchange'''
        self.size = size

    def changeDimensions(self, _, dimensions):
        '''Called by selector onchange'''
        self.dimensions = dimensions


class World():
    '''Handles in-game abstractions'''
    def __init__(self, dimensions, size):
        dimensionCenter = int(size / 2)
        self.dimensions = dimensions
        self.dimensionRange = range(dimensions)
        self.goal = self.generateGoal()
        self.playerLocation = tuple(dimensionCenter for x in range(dimensions))
        self.size = size

    def generateGoal(self):
        '''Sets the goal at the beginning of the game'''
        return tuple(randInt(self.size) for x in self.dimensionRange)

    def movePlayer(self, movement):
        '''Pretty much all the controls are hooked here.'''
        return tuple(
            adjustToBoundaries(self.playerLocation[x] + movement[x], self.size - 1)
            for x in movement
            )


def adjustToBoundaries(coordinate, boundary):
    '''Keeps the player from leaving the game area'''
    return boundary if coordinate > boundary else 0 if coordinate < 0 else coordinate

def eatFood():
    '''Victory message'''
    with open('foods.txt', 'r') as foodsFile:
        foods = [foodsFile]
    food = foods[randInt(len(foods))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')

def generateNumericalSelector(minSize, maxSize):
    '''Helper function for Game.showMenu()'''
    return [(str(x), x) for x in range(minSize, maxSize + 1)]

def getDifference(int1, int2):
    '''To shorten an unweildy list comprehension'''
    return abs(int1 - int2)

def getDistance(addressA, addressB):
    '''In Cartesian space using tuples'''
    distances = tuple(getDifference(addressA[x], addressB[x]) for x in range(len(addressA)))
    totalDistance = math.hypot(*distances)
    return totalDistance

def runMenu():
    '''Allows manual selection of world size; world dimensions are set to 2.'''
    menu = pygame_menu.Menu(
        'Welcome',
        300,
        400,
        theme=pygame_menu.themes.THEME_BLUE
        )
    menu.add.selector(
        'World size:',
        generateNumericalSelector(3, 10),
        onchange=buildWorld.changeSize # passes <option text>, <option value>
        )
    menu.add.button('Begin', pygame_menu.events.CLOSE)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

def getVelocity(goal, firstAddress, secondAddress):
    '''The player gets a readout of this.'''
    firstDistance = getDistance(firstAddress, goal)
    secondDistance = getDistance(secondAddress, goal)
    velocity = secondDistance - firstDistance
    return velocity

def randInt(maximum):
    '''Supposed to be faster than randrange'''
    return int(random() * maximum)

if __name__ == '__main__':
    # Prime game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set world attributes
    buildWorld = BuildWorld()
    runMenu()
    gameWorld = World(buildWorld.dimensions, buildWorld.size)

    # Run the game
    running = True
    while running:
        oldAddress = gameWorld.playerLocation
        gameWorld.playerLocation = gameWorld.movePlayer(tuple(randInt(3) - 1
            for x in gameWorld.dimensionRange))
        if oldAddress == gameWorld.playerLocation:
            running = False
        else:
            playerVelocity = getVelocity(gameWorld.goal, oldAddress, gameWorld.playerLocation)
            print(playerVelocity) # for testing; pipe to display

    # Win
    pygame.quit() # change to return to menu
    eatFood()
