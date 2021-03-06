import random

class Maus:
    def __init__(self, worldDimensions, worldSize):
        self.loc = dict()
        for i in range(worldDimensions):
            self.loc[i] = int(worldSize / 2) # placing the maus in the middle of the world

def win():
    with open('foods.txt', 'r') as foodsFile:
        foodsList = [x for x in foodsFile]
    food = foodsList[random.randrange(len(foodsList))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')

def newGoal(worldDimensions, worldSize):
    addressList = []
    for dummy in range(worldDimensions):
        addressList.append(random.randrange(worldSize))
    addressTuple = tuple(addressList)
    return addressTuple