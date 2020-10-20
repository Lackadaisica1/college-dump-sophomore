def build_map(fileLocation):
    mapFile = open(fileLocation, 'r')
    linesOfFile = mapFile.readlines()
    for index in range(len(linesOfFile)):
        linesOfFile[index] = linesOfFile[index].strip()
        linesOfFile[index] = linesOfFile[index].split()

    #removing the bad lines
    nuList = []
    for line in linesOfFile:
        if "#" not in line and line != "":
            nuList.append(line)

    for line in nuList:
        assert (len(line) == 2)
        assert (len(line[0]) == 1)
        assert (len(line[1]) == 1)



    subsitutionDict = {}

    for line in nuList:
        subsitutionDict[line[0]] = line[1]

    return subsitutionDict


fileLocation = input()

print(build_map(fileLocation))
