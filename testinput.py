""" File: twine.py
    Author: Abraham Aruguete
    Purpose: So this creates a game in which we use a stack to keep track of location and such. The stack which we use is encoded as a list within python. Use list.append() and list.pop() to modify the "stack" """
import sys

def input_prompt():
    """ This is a function which takes in the user input, and then relays the prompt as described in the project description. """
    lines_of_obstacle_file = []
    while True:
        #this loop is meant to be broken
        filename = input("Please give the name of the obstacles filename, or - for none.\n")
        try:
            if filename == "-":
                break
            else:
                obsFile = open(filename, "r")
                linesOfObstacleFile = obsFile.readlines()
                for i in range(len(linesOfObstacleFile)):
                    linesOfObstacleFile[i] = linesOfObstacleFile[i].strip()
                break
        except FileNotFoundError:
            print("ERROR: File not found.")
            continue

    if error_check(lines_of_obstacle_file):
        print("ERROR: Obstacle file has invalid entries.")
        sys.exit()

    terminal_commands(lines_of_obstacle_file)

def error_check(lines_of_obstacle_file):
    """ This is a function which takes in the lines of the obstacle file, error checks the lines in the obstacle file, and then either prints out an error message or continues onto the main terminal if no errors are found. """
    errorFlag = False
    #check if the lines_of_obstacle_file is empty
    if lines_of_obstacle_file == []:
        return errorFlag
    for i in range(len(lines_of_obstacle_file)):
        lines_of_obstacle_file[i] = lines_of_obstacle_file[i].split()
    for i in range(len(lines_of_obstacle_file)):
        if len(lines_of_obstacle_file[i]) > 2:
            errorFlag = True
        for j in lines_of_obstacle_file[i]:
            try:
                if (lines_of_obstacle_file[i][j] != ""):
                    int(lines_of_obstacle_file[i][j])
            except ValueError:
                errorFlag = True

    return errorFlag

def terminal_commands(lines_of_obstacle_file):
    """ This is a function which takes in the lines of the obstacle file, then edits them through a list of commands which do things to the stack."""
    # creating some lists of tuples because it makes the printing easier
    stack = [(0, 0)]
    for i in range(len(lines_of_obstacle_file)):
        lines_of_obstacle_file[i] = lines_of_obstacle_file[i].split()
    list_of_obstacle_tuples = []
    for i in range(len(lines_of_obstacle_file)):
        list_of_obstacle_tuples.append((lines_of_obstacle_file[0], lines_of_obstacle_file[1]))
    try:
        for line in sys.stdin:
            command = line
            command = command.strip()
            if(command == "n"):
                if((stack[len(stack)-1][0], stack[len(stack)-1][1] + 1) in list_of_obstacle_tuples):
                    print("You could not move in that direction, because there is an obstacle in the way.")
                    print("You stay where you are.")
                    continue
                else:
                    pos_tuple = (stack[len(stack)-1][0], stack[len(stack)-1][1] + 1)
                    stack.append(pos_tuple)
                    continue
            elif(command == "s"):
                if((stack[len(stack)-1][0], stack[len(stack)-1][1] - 1) in list_of_obstacle_tuples):
                    print("You could not move in that direction, because there is an obstacle in the way.")
                    print("You stay where you are.")
                    continue
                else:
                    pos_tuple = (stack[len(stack)-1][0], stack[len(stack)-1][1] - 1)
                    stack.append(pos_tuple)
                    continue
            elif(command == "w"):
                if((stack[len(stack)-1][0]-1, stack[len(stack)-1][1]) in list_of_obstacle_tuples):
                    print("You could not move in that direction, because there is an obstacle in the way.")
                    print("You stay where you are.")
                    continue
                else:
                    pos_tuple = (stack[len(stack)-1][0]-1, stack[len(stack)-1][1])
                    stack.append(pos_tuple)
                    continue
            elif(command == "e"):
                if((stack[len(stack)-1][0]+1, stack[len(stack)-1][1]) in list_of_obstacle_tuples):
                    print("You could not move in that direction, because there is an obstacle in the way.")
                    print("You stay where you are.")
                    continue
                else:
                    pos_tuple = (stack[len(stack)-1][0]+1, stack[len(stack)-1][1])
                    stack.append(pos_tuple)
                    continue
            elif(command == "back"):
                if (len(stack) == 1):
                    print("Cannot move back, as you are at the start!")
                    continue
                else:
                    stack.pop()
                    print("You retrace your steps by one space")
                    continue
            elif(command == ""):
                print("You do nothing.")
                continue
            elif(command == "crossings"):
                print("There have been " + str(crossings(stack)) + " times in the history when you were at this point.")
                continue
            elif(command == "ranges"):
                ranges(stack)
                continue
            elif(command == "map"):
                map(stack, list_of_obstacle_tuples)
                continue
            else:
                print("ERROR: Invalid Command.")
                continue
    except ValueError:
        print("ERROR: Invalid data type.")
            

def print_prompt(stack):
    """ This is a function which prints the features of the stack as required in the prompt. """
    print("Current Position: " + str(stack[len(stack)-1]))
    print("Your History:" + " "*5 + str(stack))
    print("What is your next command?")
        
def crossings(stack):
    """This is a function which counts the number of times you have been at the spot you are at currently."""
    count = 0
    for i in stack:
        if i == stack[len(stack)-1]:
            count += 1
    return count


def ranges(stack):
    """This is a function which takes the smallest x value, the smallest y value, the largest x value, and the largest y value, and
prints them all out (again in accordance with the ranges needed for the map)."""
    listOfXValues = []
    listOfYValues = []
    for i in stack:
        listOfXValues.append(i[0])
        listOfYValues.append(i[1])
    print("The furthest West you have ever walked is " +str(min(listOfXValues)))
    print("The furthest East you have ever walked is " + str(max(listOfXValues)))
    print("The furthest South you have ever walked is " + str(min(listOfYValues)))
    print("The furthest North you have ever walked is " + str(max(listOfYValues)))


def map(stack, listOfObstacleTuples):
    """This function prints a map in accordance with the specifics in the prompt."""
    listOfXValues = []
    listOfYValues = []
    for i in stack:
        listOfXValues.append(i[0])
        listOfYValues.append(i[1])
    SOffset = min(listOfYValues)
    NOffset = max(listOfYValues)
    EOffset = max(listOfXValues)
    WOffset = min(listOfXValues)
    grid = []
    for y in range(NOffset-SOffset):
        grid.append([])
    for x in grid:
        for j in range(EOffset-WOffset):
            x.append(".")
    grid[SOffset][WOffset] = "*"
    grid[SOffset-1 + stack[len(stack)-1][1]][WOffset-1 + stack[len(stack)-1][0]] = "+"
    for i in range(len(stack)-1):
        grid[SOffset-1 + stack[i][1]][WOffset-1 + stack[i][0]] = "X"
    for i in range(len(listOfObstacleTuples)):
         grid[SOffset-1 + listOfObstacleTuples[i][1]][WOffset-1 + listOfObstacleTuples[i][0]] = " "
    for y in grid:
        for x in y:
            print(x)
        print()
    print(grid)
    
    
    
def main():
    input_prompt()


main()
