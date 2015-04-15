__author__ = 'Milly'

import os
import csv


class FilterCsvFile():
    def __init__(self):
        pass

    @staticmethod
    def process(inputfilepath, indexToOmit):
        outputfilepath = os.path.splitext(inputfilepath)[0] + '_filtered' + os.path.splitext(inputfilepath)[1]
        with open(inputfilepath, 'rb') as csvfile, open(outputfilepath, 'wb') as myFilteredFile:
            reader = csv.reader(csvfile, delimiter=';')
            writer = csv.writer(myFilteredFile, delimiter=';')
            for line in reader:
                filteredWords = line[:indexToOmit] + line[indexToOmit + 1:]
                writer.writerow(filteredWords)
        return outputfilepath