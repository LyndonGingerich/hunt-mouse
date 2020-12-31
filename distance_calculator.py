# To do:
# Generate positions
# Build or import speedometer

import math

def pythagoreanDistance(dis1, dis2):
    hypotenuse = math.sqrt(math.pow(dis1, 2) + math.pow(dis2, 2))
    return hypotenuse

def dimensionalDistance(distances):
    # <distances> should be an iterable of numbers.
    currentDistance = 0
    for i in distances:
        currentDistance = pythagoreanDistance(currentDistance, i)
    return currentDistance
