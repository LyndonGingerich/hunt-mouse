import random

def buildGrid(grid, dimensions, size):
    # <grid> must be a list.
    # <dimensions> and <size> must be integers.
    for i in range(size):
        grid.append([])
    newDimensions = dimensions - 1
    if newDimensions > 0:
        for i in grid:
            buildGrid(i, newDimensions, size)
    return grid

def chooseItem(grid):
    chooseIndex = random.randrange(len(grid))
    goalItem = grid[chooseIndex]
    if len(goalItem) > 0:
        return chooseItem(goalItem)
    else:
        return goalItem

def printGrid(grid):
    for i in grid:
        if len(i[0]) > 0 and not i[0][0] == 'x':
            printGrid(i)
        else:
            print(i)

worldShell = []
world = buildGrid(worldShell, 3, 10)
chooseItem(world).append('x')
printGrid(world)