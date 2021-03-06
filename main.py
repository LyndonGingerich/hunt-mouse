import math
import random

class Maus:
    def __init__(self, worldDimensions, worldSize):
        self.loc = dict()
        for i in range(worldDimensions):
            self.loc[i] = int(worldSize / 2) # placing the maus in the middle of the world
        self.worldDimensions = worldDimensions
        self.worldSize = worldSize
        self.goal = generateGoal(worldDimensions, worldSize)

    def getAddress(self):
        worldDimensions = self.worldDimensions
        addressList = []
        for i in range(worldDimensions):
            addressList.append(self.loc[i])
        addressTuple = tuple(addressList)
        return addressTuple

    def move(self, movement = dict): # returns velocity
        oldAddress = self.getAddress()
        for i in range(self.worldSize):
            self.loc[i] += movement[i]
        newAddress = self.getAddress()
        velocity = getVelocity(self.goal, oldAddress, newAddress)
        return velocity

    def moveDown(self):
        return self.moveOneInTwoDimensions(1, -1)

    def moveLeft(self):
        return self.moveOneInTwoDimensions(0, -1)

    def moveRight(self):
        return self.moveOneInTwoDimensions(0, 1)

    def moveOneInTwoDimensions(self, dimension, distance):
        dimensions = self.worldDimensions
        movement = dict()
        for i in dimensions:
            movement[i] = 0
        movement[dimension] = distance
        return self.move(movement)

    def moveUp(self):
        return self.moveOneInTwoDimensions(1, 1)

def getDistance(pointA = tuple, pointB = tuple):
    if len(pointA) == len(pointB):
        distances = []
        for index, dummy in enumerate(pointA):
            distance = abs(pointA[index] - pointB[index])
            distances.append(distance)
        totalDistance = math.hypot(*distances)
        return totalDistance
    else:
        return None

def getVelocity(goal, oldAddress, newAddress):
    oldDistance = getDistance(oldAddress, goal)
    newDistance = getDistance(newAddress, goal)
    velocity = abs(oldDistance - newDistance)
    return velocity

def generateGoal(worldDimensions, worldSize):
    addressList = []
    for dummy in range(worldDimensions):
        addressList.append(random.randrange(worldSize))
    addressTuple = tuple(addressList)
    return addressTuple

def eatFood():
    with open('foods.txt', 'r') as foodsFile:
        foodsList = [x for x in foodsFile]
    food = foodsList[random.randrange(len(foodsList))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')