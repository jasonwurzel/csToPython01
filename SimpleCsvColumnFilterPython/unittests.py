from filter import FilterCsvFile
import unittest
import os


class FilterThirdColumnFromCsvFile(unittest.TestCase):
    def testDummy(self):
        # arrange
        testBasePath = os.path.join(os.path.split(os.path.split(__file__)[0])[0], 'Tests','FilterThirdCol')
        inputFilePath = os.path.join(testBasePath, 'input.csv')
        expectedfilepath = os.path.join(testBasePath, 'expected.csv')
        #act
        outputFilePath = FilterCsvFile.process(inputFilePath, 2)
        #assert
        with open(expectedfilepath) as expectedFile, open(outputFilePath) as outputFile:
            expectedContent = expectedFile.read().replace('\n', '')
            outputContent = outputFile.read().replace('\n', '')
            assert outputContent==expectedContent
        os.remove(outputFilePath)


if __name__ == "__main__":
    unittest.main()