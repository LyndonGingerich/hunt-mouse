'''The game backend, and also frontend.'''

import math
from random import random
import pygame
import pygame_menu

import controls


class Game:
    '''Runs the game and calls all the other classes'''
    def __init__(self):
        pygame.init()
        self.running = True
        self.maus = None
        self.screen = pygame.display.set_mode((600, 400))
        worldDimensions, worldSize = self.getPlayerSelectionsFromMenu()
        self.world = World(worldDimensions, worldSize)

    def playGame(self):
        '''The boss function of the boss class.'''
        while self.running:
            oldAddress = self.maus.loc
            self.maus.loc = self.maus.move(tuple(randInt(3) - 1
             for x in self.maus.dimensionRange))
            if oldAddress == self.maus.loc:
                eatFood()
                self.running = False
            else:
                velocity = getVelocity(self.maus.goal, oldAddress, self.maus.loc)
                print(velocity)

    def getPlayerSelectionsFromMenu(self):
        '''Allows manual selection of world size; world dimensions are set to 2.'''
        worldDimensions = 2
        worldSizeSelector = (None, None)
        menu = pygame_menu.Menu('Welcome', 300, 400, theme=pygame_menu.themes.THEME_BLUE)
        menu.add.selector(
            'World size:',
            generateNumericalSelector(3, 10),
            onreturn=worldSizeSelector
            )
        (_, worldSize) = worldSizeSelector
        menu.add.button('Begin', self.playGame) # not when self.playGame should be called
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(self.screen)
        return worldDimensions, worldSize


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
        goalAddress = tuple(randInt(self.size) for x in self.dimensionRange)
        return goalAddress

    def movePlayer(self, movement):
        '''Pretty much all the controls are hooked here.'''
        newAddress = tuple(adjustToBoundaries(self.playerLocation[x] + movement[x], self.size - 1)
        for x in movement)
        return newAddress


def adjustToBoundaries(coordinate, boundary):
    '''Keeps the player from leaving the game area'''
    coordinate = boundary if coordinate > boundary else 0 if coordinate < 0 else coordinate
    return coordinate

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
    difference = abs(int1 - int2)
    return difference

def getDistance(addressA, addressB):
    '''In Cartesian space using tuples'''
    distances = tuple(getDifference(addressA[x], addressB[x]) for x in range(len(addressA)))
    totalDistance = math.hypot(*distances)
    return totalDistance

def getVelocity(goal, oldAddress, newAddress):
    '''The player gets a readout of this.'''
    oldDistance = getDistance(oldAddress, goal)
    newDistance = getDistance(newAddress, goal)
    velocity = newDistance - oldDistance
    return velocity

def randInt(maximum):
    '''Supposed to be faster than randrange'''
    integer = int(random() * maximum)
    return integer

if __name__ == '__main__':
    game = Game()
