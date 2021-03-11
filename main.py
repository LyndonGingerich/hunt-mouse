import math
import pygame
# from pygame.locals import *
import random

class App:
    pass

class Maus:
    def __init__(self, worldDimensions = int, worldSize = int):
        dimensionCenter = int(worldSize / 2)
        self.loc = tuple([dimensionCenter for x in range(worldDimensions)])
        self.worldDimensions = worldDimensions
        self.worldSize = worldSize
        self.goal = Maus.generateGoal(self)

    def eatFood(self):
        with open('foods.txt', 'r') as foodsFile:
            foodsList = [x for x in foodsFile]
        food = foodsList[random.randrange(len(foodsList))]
        food = food.rstrip('\n')
        print(f'The mouse finds {food} and scarfs it down. Good job!')

    def generateGoal(self):
        goalAddress = tuple([random.randrange(self.worldSize) for x in range(self.worldDimensions)])
        return goalAddress

    def getAddress(self):
        address = tuple([self.loc[x] for x in range(self.worldDimensions)])
        return address

    def move(self, movement): # returns velocity
        oldAddress = self.getAddress()
        newAddress = tuple([oldAddress[x] + movement[x] for x in oldAddress])
        self.loc = newAddress
        velocity = getVelocity(self.goal, oldAddress, newAddress)
        return velocity

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

    def keypadMove(self, dimension0, dimension1):
        movement = (dimension0, dimension1)
        return super().move(movement)

    def moveUp(self):
        return self.keypadMove(1, 1)

    def moveUpLeft(self):
        return self.keypadMove(-1, 1)

    def moveUpRight(self):
        return self.keypadMove(1, 1)

def getDifference(int1, int2):
    difference = abs(int1 - int2)
    return difference

def getDistance(addressA = tuple, addressB = tuple):
    if len(addressA) == len(addressB):
        distances = tuple([getDifference(addressA[x], addressB[x]) for x in range(len(addressA))])
        totalDistance = math.hypot(*distances)
        return totalDistance
    else:
        return None

def getVelocity(goal, oldAddress, newAddress):
    oldDistance = getDistance(oldAddress, goal)
    newDistance = getDistance(newAddress, goal)
    velocity = newDistance - oldDistance
    return velocity