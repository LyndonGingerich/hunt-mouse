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

def getMausAddress(maus, worldDimensions):
    addressList = []
    for i in range(worldDimensions):
        addressList.append(maus.loc[i])
    addressTuple = tuple(addressList)
    return addressTuple

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