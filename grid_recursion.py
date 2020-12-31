# Uses "grid" rather than "list" as variable to avoid changing built-in terms

import random

def buildGrid(dimensions, size):
    # <grid> must be a list.
    # <dimensions> and <size> must be integers.
    grid = []
    for i in range(size):
        grid.append([])
    newDimensions = dimensions - 1
    if newDimensions > 0:
        for i in grid:
            buildGrid(i, newDimensions, size)
    return grid

def randomLocation(grid):
    chooseIndex = random.randrange(len(grid))
    goalItem = grid[chooseIndex]
    if len(goalItem) > 0:
        return chooseItem(goalItem)
    else:
        return goalItem

def printGrid(grid): # For visualization, but may come in handy for graphics when dimensions > 2
    for i in grid:
        if len(i[0]) > 0 and not i[0][0] == 'x':
            printGrid(i)
        else:
            print(i)

def insertItem(item, grid):
    randomLocation(grid).append(item)
    return grid
