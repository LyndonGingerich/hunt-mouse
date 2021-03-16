import math
import pygame
# from pygame.locals import *
import random

dimensions = 3
size = 5

class App:
    def __init__(self):
        maus = Maus(dimensions, size)
        for dummy in range(10): # for testing; will be changed to while-loop
            oldAddress = maus.loc
            newAddress = maus.move(tuple([random.randrange(3) - 1 for x in range(maus.worldDimensions)]))
            maus.loc = newAddress
            velocity = getVelocity(maus.goal, oldAddress, newAddress)
            print(velocity)

class Maus:
    def __init__(self, worldDimensions, worldSize):
        dimensionCenter = int(worldSize / 2)
        self.loc = tuple([dimensionCenter for x in range(worldDimensions)])
        self.worldDimensions = worldDimensions
        self.worldSize = worldSize
        self.goal = Maus.generateGoal(self)

    def eatFood(self):
        with open('foods.txt', 'r') as foodsFile:
            foods = [x for x in foodsFile]
        food = foods[random.randrange(len(foods))]
        food = food.rstrip('\n')
        print(f'The mouse finds {food} and scarfs it down. Good job!')

    def generateGoal(self):
        goalAddress = tuple([random.random() * self.worldSize for x in range(self.worldDimensions)])
        return goalAddress

    def move(self, movement): # returns velocity
        newAddress = tuple([self.loc[x] + movement[x] for x in movement])
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