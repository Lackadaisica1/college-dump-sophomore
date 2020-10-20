""" File: subs_cipher.py
    Author: Abraham Aruguete
    Purpose: This actually applies the cipher to a given string. It contains two functions, encode and decode."""

import build_map

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


def encode(subsitutionMap, inputString):
    """ This is a function which takes in the string and then encodes it using the values in the given subsitution map."""

    encodedString = ""

    assert is_valid_map(subsitutionMap)

    inputStringList = list(inputString)

    for index in range(len(inputStringList)):
        if inputStringList[index] in subsitutionMap.keys():
            inputStringList[index] = subsitutionMap[inputStringList[index]]


    for char in inputStringList:
        encodedString += char
        
    return encodedString
            
def decode(subsitutionMap, inputString):
    """ This does the same thing, but in the reverse order, values -> keys """
    encodedString = ""

    assert is_valid_map(subsitutionMap)
    reverseSubsitutionMap = {}

    for key, value in subsitutionMap.items():
        reverseSubsitutionMap[value] = key

    inputStringList = list(inputString)

    for index in range(len(inputStringList)):
        if inputStringList[index] in reverseSubsitutionMap.keys():
            inputStringList[index] = reverseSubsitutionMap[inputStringList[index]]

    for char in inputStringList:
        encodedString += char
        
    return encodedString
