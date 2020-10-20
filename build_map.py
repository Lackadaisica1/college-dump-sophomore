""" File: build_map.py
    Author: Abraham Aruguete
    Purpose: This function deals with building and checking maps for the subsitution cipher. It contains at least two functions: build_map() and is_valid_map()."""

def build_map(fileLocation):
    """ This function takes a fileLocation and then creates a dictionary out of it """
    mapFile = open(fileLocation, 'r')
    linesOfFile = mapFile.readlines()
    for index in range(len(linesOfFile)):
        linesOfFile[index] = linesOfFile[index].strip()
        linesOfFile[index] = linesOfFile[index].split()

    #removing the bad lines
    nuList = []
    for line in linesOfFile:
        if "#" not in line and len(line) != 0:
            nuList.append(line)


    fromSet = set()

    
    for line in nuList:
        assert (len(line) == 2)
        assert (len(line[0]) == 1)
        assert (len(line[1]) == 1)
        assert line[0] not in fromSet
        fromSet.add(line[0])

        
    subsitutionDict = {}

    for line in nuList:
        subsitutionDict[line[0]] = line[1]

    return subsitutionDict


def is_valid_map(subsitutionDict):
    """ This function checks if the subsitutionDict returned from build_map is valid or not. """

    #create two sets which will contain the from and to characters
    setFrom = set()
    setTo = set()

    #create a flag which starts as true but will return false if one of the conditions
    #returns 0
    flagAssert = True

    listTo = subsitutionDict.values()
    listFrom = subsitutionDict.keys()

    
    # uniqueness condition check
    for char in listTo:
        if char in setTo:
            flagAssert = False
            break
        else:
            setTo.add(char)

    for char in listFrom:
        if char in setFrom:
            flagAssert = False
            break
        else:
            setFrom.add(char)


    # and now to check the first three conditions
    for char in setTo:
        if(type(char) != str):
            flagAssert = False
            break
        elif (len(char) != 1):
            flagAssert = False
            break
        elif char in " \t\n":
            flagAssert = False
            break

    for char in setFrom:
        if(type(char) != str):
            flagAssert = False
            break
        elif (len(char) != 1):
            flagAssert = False
            break
        elif char in " \t\n":
            flagAssert = False
            break


    return flagAssert
