import os
import re


def main():
    allFilesInCWD = os.listdir(os.getcwd())
    fileRegex = re.compile(r'.*.txt')

    textFilesinDir = []
    for filetoSearch in allFilesInCWD:
        textFile = fileRegex.search(filetoSearch)
        if textFile != None:
            textFilesinDir.append(textFile)


main()
