def appendFour(appendList, character):
    for i in range(3):
        appendList.append(character)
    return appendList

def printEdge(columns):
    characters = []
    characters.append('+')
    for i in range(columns - 1):
        appendFour(characters, '-')
        characters.append('+')
    line = ' '.join(characters)
    print(line)

def printInterior(columns):
    characters = []
    characters.append('|')
    for i in range(columns - 1):
        appendFour(characters, ' ')
        characters.append('|')
    line = ' '.join(characters)
    print(line)

def printGrid(columns, rows):
    printEdge(columns)
    for i in range(rows - 1):
        for i in range(3):
            printInterior(columns)
        printEdge(columns)

printGrid(4, 4)
