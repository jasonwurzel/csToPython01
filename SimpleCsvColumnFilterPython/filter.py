__author__ = 'Milly'
index = 2
with open('filename') as myFile:
    lines = [line.rstrip('\n') for line in myFile]
    filteredLines = []
    for line in lines:
        words = line.split(';')
        filteredWords = []
        for w in words[0:index]:
            filteredWords.append(w)
        for w in words[index:len(words)]:
            filteredWords.append(w)
        filteredLine = ";".join(filteredWords)
        filteredLines.append(filteredLine)
