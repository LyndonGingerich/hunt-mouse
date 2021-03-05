import navigation
import newworld
import random

class Maus:
    def __init__(self, *coordinates):
        self.loc = list(coordinates)

worldDimensions = int(input('Number of dimensions: '))
worldLength = int(input('World size in cells: '))
world = newworld.newWorld(worldDimensions, worldLength)

def win():
    with open('foods.txt', 'r') as foodsFile:
        foodsList = [x for x in foodsFile]
    food = foodsList[random.randrange(len(foodsList))]
    food = food.rstrip('\n')
    print(f'The mouse finds {food} and scarfs it down. Good job!')