""" File: unzip.py
    Author: Abraham Aruguete
    Purpose: To unzip a given command stream as mentioned in the prompt."""



def unzip(compressed_stream):
    """ Unzips the compressed stream and then returns an uncompressed string. """
    #this is the assert(s) block
    for entry in compressed_stream:
        assert (type(entry) == str) or (type(entry) == tuple)
        if (type(entry) == str):
            assert len(entry) == 1
        elif (type(entry) == tuple):
            assert len(entry) == 2
            assert type(entry[0]) == int
            assert type(entry[1]) == int
            assert entry[0] > 0
            assert entry[1] > 0

    uncompressedString = ""
    sliceOfWord = []

    for entry in compressed_stream:
        if type(entry) == str:
            uncompressedString += entry
        elif type(entry) == tuple:
            sliceOfWord = str(uncompressedString[len(uncompressedString) - entry[0]:len(uncompressedString) - entry[0] + entry[1]])
            uncompressedString += sliceOfWord

            assert entry[0] < len(uncompressedString)

            

    return uncompressedString
        
