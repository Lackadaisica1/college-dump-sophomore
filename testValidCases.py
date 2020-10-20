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


    



print(compare_front("asdf", "ackbar"))
print(compare_back([10, -1, 0, 127, 12, 13], ["asdf", 12, 13]))
print(compare_front("ass", "titties")) # should return 0
print(compare_back("aaaaaaa", "aaaaaa")) # should return 6
print(compare_front("a", "a"))
print(compare_front("aa", "aa"))
print(compare_front("aaac", "aaa"))
