# Uses "grid" rather than "list" as variable to avoid changing built-in terms

import random

goalItem = 'x'

def buildGrid(grid: list, dimensions: int, size: int):
    for i in range(size):
        grid.append([])
    newDimensions = dimensions - 1
    if newDimensions > 0:
        for i in grid:
            buildGrid(i, newDimensions, size)
    return grid

def randomLocation(grid):
    chooseIndex = random.randrange(len(grid))
    goalIndex = grid[chooseIndex]
    if len(goalIndex) > 0:
        return randomLocation(goalIndex)
    else:
        return goalIndex

def printGrid(grid): # For visualization, but may come in handy for graphics when dimensions > 2
    for i in grid:
        if len(i[0]) > 0 and i[0][0] != goalItem:
            printGrid(i)
        else:
            print(i)

def insertGoalItem(grid):
    randomLocation(grid).append(goalItem)
    return grid
