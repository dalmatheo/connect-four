grid = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
]

teams = ['red', 'yellow']

def resetGrid():
        """
        Reset the grid to its original 7*6 form without colors.

        Returns:
            list: Returns the colors.
        """
        global grid
        grid = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
        ]

def getTeams():
    """
    Returns all the possible teams.

    Returns:
        list: Returns the colors.
    """
    return teams

def getTeam(index):
    """
    Returns the specified team.

    Argument:
        index (number): The index of the desired team.

    Returns:
        string: Returns the desired team.
    """
    return getTeams()[index]


def setTeam(index, color):
    teams[index] = color

def getLines():
    """
    Returns all lines from 0 to n.

    Returns:
        list: Returns a list containing all lines.
    """
    lines = []
    for line in grid:
        lines.append(line)
    lines.reverse()
    return lines


def getLine(index):
    """
    Returns the specified line.

    Argument:
        index (number): The index of the desired line.

    Returns:
        list: Returns the desired line.
    """
    return getLines()[index]


def getCollumns():
    """
    Returns all collumns from 0 to n.

    Returns:
        list: Returns a list containing all collumns.
    """
    collones = [[], [], [], [], [], [], []]
    for line in grid:
        for i in range(len(line)):
            collones[i].append(line[i])
    return collones


def getCollumn(index):
    """
    Returns the specified collumn.

    Argument:
        index (number): The index of the desired collumn.

    Returns:
        list: Returns the desired collumn.
    """
    return getCollumns()[index]


def placeColor(color, n):
    """
    Place the 'color' at the 'n' collumn

    Argument:
        color (string): The color that will be placed.
        n (number): The collumn in which the color should be placed.
    """
    for line in grid:
        if line[n] == " ":
            line[n] = color
            return True


def checkWin(color):
    """
    Check if the 'color' won.

    Argument:
        color (string): The color that might've won.

    Returns:
        boolean: Returns True if 'color' won.
    """
    flag = False
    for line in getLines():
        suite = 0
        for case in line:
            if case == color:
                suite += 1
                if suite >= 4:
                    flag = True
                    break
            else:
                suite = 0
    for col in getCollumns():
        suite = 0
        for case in col:
            if case == color:
                suite += 1
                if suite >= 4:
                    flag = True
                    break
            else:
                suite = 0
    for line_number in range(len(grid)):
        for case_number in range(len(getLine(line_number))):
            suite = 0
            for n in range(4):
                if line_number + n > 5 or case_number + n > 6:
                    break
                elif getLine(line_number + n)[case_number + n] == color:
                    suite += 1
                    if suite >= 4:
                        flag = True
                        break
                else:
                    suite = 0
            suite = 0
            for n in range(4):
                if line_number - n < 0 or case_number + n > 6:
                    break
                elif getLine(line_number - n)[case_number + n] == color:
                    suite += 1
                    if suite >= 4:
                        flag = True
                        break
                else:
                    suite = 0
    return flag
