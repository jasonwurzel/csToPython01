from filter import process
import unittest
import os


class FilterThirdColumnFromCsvFile(unittest.TestCase):
    def testDummy(self):
        # arrange
        inputFilePath = 'C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\input.csv'
        expectedFilePath = 'C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\expected.csv'
        #act
        outputFilePath = process(inputFilePath, 2)
        #assert
        with open(expectedFilePath) as expectedFile, open(outputFilePath) as outputFile:
            expectedContent = expectedFile.read().replace('\n', '')
            outputContent = outputFile.read().replace('\n', '')
            assert outputContent==expectedContent
        os.remove(outputFilePath)


if __name__ == "__main__":
    unittest.main()