""" File: rhymes.py
    Author: Abraham Aruguete
    Purpose: This script contains a function which takes in an input dictionary, a given word, and then prints out a bunch of words which rhyme with the word. """



def prompt_user():
    """ Prompt the user for the filename, and then open the filename and parse through the information. """

    #preform the check as outlined in the first part of the prompt
    filename = input()
    dictFile = open(filename, "r")
    linesOfDictFile = dictFile.readlines()
    for line in linesOfDictFile:
        line = line.strip()


    # convert each line in linesOfDictFile into a split list
    for index in range(len(linesOfDictFile)):
        linesOfDictFile[index] = linesOfDictFile[index].split()



    #remove the undesirables from the list at hand
    index = 0
    

    while index < len(linesOfDictFile):
        if linesOfDictFile[index] == []:
            del linesOfDictFile[index]
            index -= 1
        index += 1


    userDict = {}

    for line in linesOfDictFile:
        userDict[line[0]] = line[1:len(line)]

    return userDict

def compare_back(linearType1, linearType2):
    """This function compares two linear types starting from the highest index of each."""

    assert type(linearType1) == type(linearType2)

    
    if (len(linearType1) <= len(linearType2)):
        indexSmaller = len(linearType1) - 1
        indexLarger = len(linearType2) - 1
    
        if not linearType1 or not linearType2:
            return 0

        charsSame = 0

        while indexSmaller >= 0 and (linearType1[indexSmaller] == linearType2[indexLarger]):
            if(linearType1[indexSmaller] == linearType2[indexLarger]):
                charsSame += 1
            if(indexSmaller == len(linearType1)):
                return len(smallerLinear)
            indexSmaller -= 1
            indexLarger -= 1

        return charsSame

    else:
        indexSmaller = len(linearType2) - 1
        indexLarger = len(linearType1) - 1

        if not linearType1 or not linearType2:
            return 0

        charsSame = 0
    
        while indexSmaller >= 0 and (linearType2[indexSmaller] == linearType1[indexLarger]):
            if(linearType2[indexSmaller] == linearType1[indexLarger]):
                charsSame += 1
            if(indexSmaller == len(linearType2)):
                return len(smallerLinear)
            indexSmaller -= 1
            indexLarger -= 1

        return charsSame

def compare_front(linearType1, linearType2):
    """ This function compares two linear types starting from index zero. """ 
    assert type(linearType1) == type(linearType2)
    i = 0
    charsSame = 0
    if (linearType1[0] != linearType2[0]):
        return 0
    if (linearType1 == linearType2):
        return len(linearType1)
    if not linearType1 or not linearType2:
        return 0
    while ((i < len(linearType1)) and (i < len(linearType2)) and (linearType1[i] == linearType2[i])):
        if(linearType1[i] == linearType2[i]):
            charsSame += 1
        if(charsSame == len(linearType1)):
            return len(linearType1)
        if(charsSame == len(linearType2)):
            return len(linearType2)
        i += 1


    return charsSame


def primary_stress(listOfStrings):
    """ This function iterates through a list of phonemes and returns the index
of the phoneme which contains the primary stress. """
    assert type(listOfStrings) == list
    assert listOfStrings != []
    for string in listOfStrings:
        assert string != ""


    flag = False
    for index in range(len(listOfStrings)):
        if len(listOfStrings[index]) > 1:
            if "1" in listOfStrings[index]:
                flag = True
                searchIndex = index
                break

    if flag:
        return searchIndex
    else:
        return None
    

def rhyme_check(rhymePhonemes, listOfPhonemes):
    """ This function takes in two lists of phonemes, compares them, and checks if they rhyme. """
    indexOfRhyme = listOfPhonemes.index(rhymePhonemes[1])
    flagRhyme = True
    if listOfPhonemes[indexOfRhyme - 1] == rhymePhonemes[0]:
        flagRhyme = False
    if indexOfRhyme - 1 < 0:
        flagRhyme = False
    frontRhyme = rhymePhonemes[1:len(rhymePhonemes)]
    frontPhonemes = listOfPhonemes[indexOfRhyme:len(listOfPhonemes)]
    charsSame = compare_front(frontRhyme, frontPhonemes)
    if charsSame != max([len(frontRhyme), len(frontPhonemes)]):
        flagRhyme = False

    return flagRhyme

   

def search_dict(word, dictionary):
    """ This function searches the dictionary for words, and then does what it does with them. """
    listOfWordPhonemes = dictionary[word]
    primaryStressIndex = primary_stress(listOfWordPhonemes)
    rhymeIndicator = listOfWordPhonemes[primaryStressIndex]

    potentialRhymeDict = {}

    for key in list(dictionary.keys()):
        if rhymeIndicator in dictionary[key]:
            potentialRhymeDict[key] = dictionary[key]

    
    forwardPhonemes = listOfWordPhonemes[primaryStressIndex:len(listOfWordPhonemes)]
    backwardPhonemes = listOfWordPhonemes[primaryStressIndex-1:primaryStressIndex]
    rhymePhonemes = backwardPhonemes + forwardPhonemes

    

    confirmedRhymeDict = {}

    #now check if each key in the potential rhyme dict is a rhyme
    for key in list(potentialRhymeDict.keys()):
        if rhyme_check(rhymePhonemes, potentialRhymeDict[key]):
            confirmedRhymeDict[key] = potentialRhymeDict[key]

    sortedRhymeList = list(confirmedRhymeDict.keys())
    sortedRhymeList = set(sortedRhymeList)
    sortedRhymeList = list(sortedRhymeList)
    sortedRhymeList = sorted(sortedRhymeList)

    print("Rhymes for: " + word.upper())

    if len(sortedRhymeList)==0:
        print("-- none found --")
        print()
    else:
        for entry in sortedRhymeList:
            print(entry.upper())
        


def main():
    dictionary = prompt_user()

    while True:
        try:
            word = input()
            if word == "":
                print("No word given")
                print()
                continue
            elif len(word.split()) > 1:
                print("Multiple words entered, please enter only one word at a time.")
                print()
                continue
            else:
                word = word.upper()
                search_dict(word, dictionary)
                continue
        except EOFError:
            break


main()
        
    
    
