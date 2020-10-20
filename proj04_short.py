""" File: proj04_short.py
    Author: Abraham Aruguete
    Purpose: So this project contains three functions which will be called by Russ' testcases. I'm actually working on writing down a pre-plan for my code instead of just rushing in there coding this time! How pleasant. I think I'm maturing. """

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
    



    
