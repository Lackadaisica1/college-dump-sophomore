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


print(primary_stress(['W', 'IY1', 'K', 'L', 'IY0'])) #should return 1
print(primary_stress(['K', 'AH0', 'M', 'P', 'Y', 'UW1', 'T', 'ER0', 'AY2', 'Z']))
#should return 5
print(primary_stress(['R', 'AH0', 'K', 'A01', 'R', 'D']))
#should return 3
print(primary_stress(['EY1', 'K']))
#should return 0
print(primary_stress(['EY0', 'K']))
#should return None
            
