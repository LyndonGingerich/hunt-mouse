# Uses "grid" rather than "list" as variable to avoid changing built-in terms

import random

goalItem = 'x'

def buildGrid(dimensions: int, size: int, grid: list = None):
    if grid == None:
        grid = []
    for i in range(size):
        grid.append([])
    newDimensions = dimensions - 1
    if newDimensions > 0:
        for i in grid:
            buildGrid(newDimensions, size, i)
    return grid

def randomLocation(grid):
    chooseIndex = random.randrange(len(grid))
    goalIndex = grid[chooseIndex]
    if len(goalIndex) > 0:
        return randomLocation(goalIndex)
    else:
        return goalIndex

def insertGoalItem(grid):
    randomLocation(grid).append(goalItem)
    return grid

def newWorld(dimensions, size):
    newGrid = buildGrid(dimensions, size)
    insertGoalItem(newGrid)
    return newGrid