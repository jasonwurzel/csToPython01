__author__ = 'Milly'
index = 2
with open('C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\input.csv') as myFile:
    lines = [line.rstrip('\n') for line in myFile]
    filteredLines = []
    for line in lines:
        words = line.split(';')
        filteredWords = []
        for w in words[0:index]:
            filteredWords.append(w)
        for w in words[index+1:len(words)]:
            filteredWords.append(w)
        filteredLine = ";".join(filteredWords)
        filteredLines.append(filteredLine + "\n")
with open('C:\Users\Milly\Documents\Visual Studio 2013\Projects\SimpleCsvColumnFilter\Tests\FilterThirdCol\input_filtered.csv', 'w' ) as myFilteredFile:
    myFilteredFile.writelines(filteredLines)
