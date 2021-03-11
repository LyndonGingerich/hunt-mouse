import math
import pygame
# from pygame.locals import *
import random

class App:
    pass

class Maus:
    def __init__(self, worldDimensions = int, worldSize = int):
        self.loc = dict()
        for i in range(worldDimensions):
            self.loc[i] = int(worldSize / 2) # placing the maus in the middle of the world
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

    def move(self, movement = dict): # returns velocity
        oldAddress = self.getAddress()
        for i in range(self.worldSize):
            self.loc[i] += movement[i]
        newAddress = self.getAddress()
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

    def keypadMove(self, dimension, distance):
        dimensions = 2
        movement = dict()
        for i in range(dimensions):
            movement[i] = 0
        movement[dimension] = distance
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

def getDistance(pointA = tuple, pointB = tuple):
    if len(pointA) == len(pointB):
        distances = tuple([getDifference(pointA[x], pointB[x]) for x in range(len(pointA))])
        totalDistance = math.hypot(*distances)
        return totalDistance
    else:
        return None

def getVelocity(goal, oldAddress, newAddress):
    oldDistance = getDistance(oldAddress, goal)
    newDistance = getDistance(newAddress, goal)
    velocity = newDistance - oldDistance
    return velocity