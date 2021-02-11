import os
import re


def main():
    allFilesInCWD = os.listdir(os.getcwd())
    fileRegex = re.compile(r'.*.txt')

    textFilesinDir = []
    # add all .txt files to be searched
    for filetoSearch in allFilesInCWD:
        textFile = fileRegex.match(filetoSearch)
        if textFile:
            textFilesinDir.append(textFile.group())
    print("Found %s Files to Search:" % len(textFilesinDir))
    print("===============================================")
    for files in textFilesinDir:
        print('* ' + files)
    print("===============================================")
    # determine custom regex:
    lookingFor = input(
        'Enter a REGEX to Search These %s Files: ' % len(textFilesinDir))
    userRegex = re.compile(r'[%s]' % lookingFor)

    print("===============================================")

    # open all files and search for user supplied Regex:
    for filetoSearch in textFilesinDir:
        # open the file
        openedFile = open(filetoSearch, 'r')

        linesOfFile = openedFile.readline()

        print("Searching \"%s\" with REGEX: %s" % (filetoSearch, lookingFor))
        print("===============================================")


main()
