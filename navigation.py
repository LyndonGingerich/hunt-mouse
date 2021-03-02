import math
from newworld import goalItem

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

def checkLoc(entity, grid, coordinates): # recursive function to check whether the current location is the goal
    pass