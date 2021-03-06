import math
import random

class Maus:
    def __init__(self, worldDimensions, worldSize):
        self.loc = dict()
        for i in range(worldDimensions):
            self.loc[i] = int(worldSize / 2) # placing the maus in the middle of the world
        self.worldDimensions = worldDimensions
        self.worldSize = worldSize
        self.goal = newGoal(worldDimensions, worldSize)

def distance(pointA = tuple, pointB = tuple):
    if len(pointA) == len(pointB):
        distances = []
        for index, dummy in enumerate(pointA):
            distance = abs(pointA[index] - pointB[index])
            distances.append(distance)
        totalDistance = math.hypot(*distances)
        return totalDistance
    else:
        return None

def getMausAddress(maus):
    worldDimensions = maus.worldDimensions
    addressList = []
    for i in range(worldDimensions):
        addressList.append(maus.loc[i])
    addressTuple = tuple(addressList)
    return addressTuple

def getVelocity(goal, oldAddress, newAddress):
    oldDistance = distance(oldAddress, goal)
    newDistance = distance(newAddress, goal)
    velocity = abs(oldDistance - newDistance)
    return velocity

def move(maus, movement = dict): # returns velocity
    oldAddress = getMausAddress(maus)
    for i in range(maus.worldSize):
        maus.loc[i] += movement[i]
    newAddress = getMausAddress(maus)
    velocity = getVelocity(maus.goal, oldAddress, newAddress)
    return velocity

def moveDown(maus):
    return moveOneInTwoDimensions(maus, 1, -1)

def moveLeft(maus):
    return moveOneInTwoDimensions(maus, 0, -1)

def moveRight(maus):
    return moveOneInTwoDimensions(maus, 0, 1)

def moveOneInTwoDimensions(maus, dimension, distance):
    dimensions = maus.worldDimensions
    movement = dict()
    for i in dimensions:
        movement[i] = 0
    movement[dimension] = distance
    return move(maus, movement)

def moveUp(maus):
    return moveOneInTwoDimensions(maus, 1, 1)

def newGoal(worldDimensions, worldSize):
    addressList = []
    for dummy in range(worldDimensions):
        addressList.append(random.randrange(worldSize))
    addressTuple = tuple(addressList)
    return addressTuple

def win():
    with open('foods.txt', 'r') as foodsFile:
        foodsList = [x for x in foodsFile]
    food = foodsList[random.randrange(len(foodsList))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')