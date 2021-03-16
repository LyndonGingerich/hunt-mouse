import math
import pygame
from random import random

dimensions = 3
size = 5

class Game:
    def __init__(self):
        self.maus = Maus(dimensions, size)
        self.running = True
    
    def playGame(self):
        while self.running == True:
            oldAddress = self.maus.loc
            self.maus.loc = self.maus.move(tuple(
                [randomInteger(3) - 1 for x in self.maus.dimensionRange]))
            if oldAddress == self.maus.loc:
                self.maus.eatFood()
                self.running = False
            else:
                velocity = getVelocity(self.maus.goal, oldAddress, self.maus.loc)
                print(velocity)

class Maus:
    def __init__(self, worldDimensions, worldSize):
        dimensionCenter = int(worldSize / 2)
        self.dimensionRange = range(worldDimensions)
        self.worldSize = worldSize
        self.goal = Maus.generateGoal(self)
        self.loc = tuple([dimensionCenter for x in self.dimensionRange])

    def eatFood(self):
        with open('foods.txt', 'r') as foodsFile:
            foods = [x for x in foodsFile]
        food = foods[randomInteger(len(foods))]
        food = food.rstrip('\n')
        print(f'The mouse finds {food} and scarfs it down. Good job!')

    def generateGoal(self):
        goalAddress = tuple([randomInteger(self.worldSize) for x in self.dimensionRange])
        return goalAddress

    def move(self, movement): # returns velocity
        newAddress = tuple([adjustToBoundaries(self.loc[x] + movement[x], self.worldSize - 1) 
        for x in movement])
        return newAddress

class ManualMaus(Maus):
    def __init__(self, worldSize):
        super().__init__(2, worldSize)

    def moveDown(self):
        return self.keypadMove(1, -1)

    def moveDownLeft(self):
        return self.keypadMove(-1, -1)

    def moveDownRight(self):
        return self.keypadMove(1, -1)

    def moveLeft(self):
        return self.keypadMove(0, -1)

    def moveRight(self):
        return self.keypadMove(0, 1)

    def keypadMove(self, *movements):
        return super().move(movements)

    def moveUp(self):
        return self.keypadMove(1, 1)

    def moveUpLeft(self):
        return self.keypadMove(-1, 1)

    def moveUpRight(self):
        return self.keypadMove(1, 1)

def adjustToBoundaries(coordinate, boundary):
    if coordinate > boundary:
        coordinate = boundary
    elif coordinate < 0:
        coordinate = 0
    return coordinate

def randomInteger(maximum): # supposed to be faster than randrange
    integer = int(random() * maximum)
    return integer

def getDifference(int1, int2):
    difference = abs(int1 - int2)
    return difference

def getDistance(addressA, addressB):
    distances = tuple([getDifference(addressA[x], addressB[x]) for x in range(len(addressA))])
    totalDistance = math.hypot(*distances)
    return totalDistance

def getVelocity(goal, oldAddress, newAddress):
    oldDistance = getDistance(oldAddress, goal)
    newDistance = getDistance(newAddress, goal)
    velocity = newDistance - oldDistance
    return velocity

if __name__ == '__main__':
    game = Game()
    game.playGame()