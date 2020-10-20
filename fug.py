""" File: fug.py
    Author: Abraham Aruguete
    Purpose: To create a grid drawing such that it emulates pixels on a screen
    or something. Graphics. Woo.
"""
import sys


def terminal():
    """ This is a function which takes in the user input, and then checks it
    among a list of valid terminal commands. """
    #current grid for most of the functions
    currentGrid = []
    commandList = []
    init_Flag = False
    for line in sys.stdin:
        if line == "":
            print("Input error: Empty File")
            sys.exit()
        if line.lstrip().startswith("#"):
            continue
        line = line.strip()
        try:
            if ("init" in line) and (init_Flag == False):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                #TODO: the actual commands within the command list
                currentGrid = init(commandList[1], commandList[2])
                init_Flag = True
                continue
            elif ("print_raw" in line) and (init_Flag == True):
                print(currentGrid)
                continue
            elif ("print" in line) and (init_Flag == True):
                print_interpreted(currentGrid)
                continue
            elif ("set" in line) and (init_Flag == True):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                commandList[3] = int(commandList[3])
                currentGrid = set_color(commandList[1], \
                                    commandList[2], commandList[3], currentGrid)
                continue
            elif ("horiz_line" in line) and (init_Flag == True):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                commandList[3] = int(commandList[3])
                commandList[4] = int(commandList[4])
                commandList[5] = int(commandList[5])
                currentGrid = horiz_line(commandList[1], commandList[2], \
                                         commandList[3], commandList[4], commandList[5], currentGrid)
                continue
            elif ("vert_line" in line) and (init_Flag == True):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                commandList[3] = int(commandList[3])
                commandList[4] = int(commandList[4])
                commandList[5] = int(commandList[5])
                currentGrid = vert_line(commandList[1], commandList[2],\
                                        commandList[3], commandList[4], commandList[5], currentGrid)
                continue
            elif ("filled_rect" in line) and (init_Flag == True):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                commandList[3] = int(commandList[3])
                commandList[4] = int(commandList[4])
                commandList[5] = int(commandList[5])
                currentGrid = filled_rectangle(commandList[1], commandList[2],\
                                               commandList[3], commandList[4], commandList[5], currentGrid)
                continue
            elif ("hollow_rect" in line) and (init_Flag == True):
                commandList = line.split()
                commandList[1] = int(commandList[1])
                commandList[2] = int(commandList[2])
                commandList[3] = int(commandList[3])
                commandList[4] = int(commandList[4])
                commandList[5] = int(commandList[5])
                currentGrid = hollow_rectangle(commandList[1], commandList[2], \
                                               commandList[3], commandList[4], commandList[5], currentGrid)
                continue
            elif ("init" in line) and (init_Flag == True):
                print("Input error: init already used. Closing...")
                sys.exit()
            else:
                print("Input error: Invalid command.")
                continue
        except ValueError:
            print("Input error: Generic.")
            continue

def init(length, height):
    """This is a function which initializes the width times length grid we are workin' with
    you know, like fucking hell holy shit a NESTED LOOP!!!!"""
    grid = []
    for x in range(height):
        grid.append([0]*length)
    return grid

def print_interpreted(grid_of_stuff):
    """This is a function which also does that thing where like you print the grid we're workin'
    with, shoopdawoop etc. Except in reverse order."""
    for i in range(len(grid_of_stuff)-1, -1, -1):
        for j in range(len(grid_of_stuff[i])):
            print(grid_of_stuff[i][j], end="")
        print()
    
#print_raw is implemented in terminal()

def set_color(color, x, y, grid):
    """ This is a function which sets the color of a given coordinate on the grid
    to a given color value. NOTE THAT the system is in the coordinate system
    described in the docs, x is the second list index, y is the first"""
    grid[y][x] = color
    return grid

def horiz_line(color, x1, x2, y1, y2, grid):
    """ This again is a function which sets the color of a given line on the grid
    to a given color value. Does some coordinate checks too to make sure everything
    is cash money."""
    if y1 == y2:
        if x1 <= x2:
            for xpos in range(x1, x2):
                grid[y1][xpos] = color
            return grid
        else:
            print("Input error: Incorrect parameters to horizontal line.")
            return grid
    else:
         print("Input error: Incorrect parameters to horizontal line.")
         return grid
            
def vert_line(color, x1, x2, y1, y2, grid):
    """Does the same thing as the above function, but with a vertical line instead."""
    if x1 == x2:
        if y1 <= y2:
            for ypos in range(y1-1, y2):
                grid[ypos][x1] = color
            return grid
        else:
            print("Input error: Incorrect parameters to vertical line.")
            return grid
    else:
        print("Input error: Incorrect parameters to vertical line.")
        return grid

            
def filled_rectangle(color, x1, y1, x2, y2, grid):
    """ This draws a rectangle of the specified color on the grid, by doing a box
       from the first corner x1, y1 to x2, y2 with the color specified in the
       parameters. """
    if x1 <= x2:
        if y1 <= y2:
            for ypos in range(y1-1, y2):
                for xpos in range(x1-1, x2):
                    grid[len(grid) - ypos][xpos] = color
            return grid
        else:
            print("Input error: Incorrect parameters to filled rectangle.")
            return grid
    else:
        print("Input error: Incorrect parameters to filled rectangle.")
        return grid



def hollow_rectangle(color, x1, y1, x2, y2, grid):
    """ This draws a hollow rectangle of the specified color on the grid, by doing
    a hollow box from the first corner x1 to the second color x2 and so on and
    so forth. """
    if x1 <= x2:
        if y1 <= y2:
           grid = horiz_line(color, x1, x2, y1, y1, grid)
           grid = horiz_line(color, x1, x2, y2, y2, grid)
           grid = vert_line(color, x1-1, x1-1, y1+1, y2+1, grid)
           grid = vert_line(color, x2-1, x2-1, y1+1, y2+1, grid)
           return grid
        else:
            print("Input error: Incorrect parameters to hollow rectangle.")
            return grid
    else:
        print("Input error: Incorrect parameters to hollow rectangle.")
        return grid

def main():
    terminal()

main()
