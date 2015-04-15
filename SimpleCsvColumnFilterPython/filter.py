__author__ = 'Milly'

import os


class FilterCsvFile():
    def __init__(self):
        pass

    @staticmethod
    def process(fileName, indexToOmit):
        with open(fileName) as myFile:
            lines = [line.rstrip('\n') for line in myFile]
            filteredLines = []
            for line in lines:
                words = line.split(';')
                filteredWords = words[:indexToOmit] + words[indexToOmit + 1:]
                filteredLine = ";".join(filteredWords)
                filteredLines.append(filteredLine + "\n")
        outputFile = os.path.splitext(fileName)[0] + '_filtered' + os.path.splitext(fileName)[1]
        with open(outputFile, 'w') as myFilteredFile:
            myFilteredFile.writelines(filteredLines)
        return outputFile