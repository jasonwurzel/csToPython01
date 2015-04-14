__author__ = 'Milly'

import os


#class FilterCsvFile():
def process(fileName, indexToOmmit):
    #with open('C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\input.csv') as myFile:
    with open(fileName) as myFile:
        lines = [line.rstrip('\n') for line in myFile]
        filteredLines = []
        for line in lines:
            words = line.split(';')
            filteredWords = words[:indexToOmmit] + words[indexToOmmit+1:]
            filteredLine = ";".join(filteredWords)
            filteredLines.append(filteredLine + "\n")
    #TODO: filenamewithoutextension + _filtered + extension
    #outputFile = 'C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\input_filtered.csv'
    outputFile = os.path.splitext(fileName)[0] + '_filtered' + os.path.splitext(fileName)[1]
    with open(outputFile, 'w' ) as myFilteredFile:
        myFilteredFile.writelines(filteredLines)
    return outputFile