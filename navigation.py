import math

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

def getMausAddress(maus, worldDimensions):
    addressList = []
    for i in range(worldDimensions):
        addressList.append(maus.loc[i])
    addressTuple = tuple(addressList)
    return addressTuple