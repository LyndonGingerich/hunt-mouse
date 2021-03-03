import math
from newworld import goalItem

def checkForContents(item):
    if item.len > 0 and item != goalItem:
        return True
    else:
        return False

def checkIfGoal(grid, entity):
    contents = getContents(grid, entity)
    if contents == goalItem:
        return True
    else:
        return False

def distance(pointA, pointB):
    # Assuming pointA and pointB are tuples
    if len(pointA) == len(pointB):
        distances = []
        for index, dummy in enumerate(pointA):
            distance = abs(pointA[index] - pointB[index])
            distances.append(distance)
        totalDistance = math.hypot(*distances)
        return totalDistance
    else:
        return None

def getContents(grid, entity): # recursive function to check whether the current location is the goal
    coordinates = entity.loc
    if checkForContents(grid):
        contents = getContents(grid[coordinates][0], coordinates.pop(0))
    else: # if it's empty
        contents = grid
    return contents