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
    userRegex = re.compile(r'%s' % lookingFor)

    print("===============================================")

    # open all files and search for user supplied Regex:
    for filetoSearch in textFilesinDir:
        # open the file
        openedFile = open(filetoSearch, 'r')

        linesOfFile = openedFile.read()

        print("Searching \"%s\" with REGEX: %s" % (filetoSearch, lookingFor))
        print("===============================================")
        count = 0
        foundItems = []
        foundInstance = userRegex.findall(linesOfFile, re.MULTILINE)
        if foundInstance:
            count += 1
            foundItems.append(foundInstance)
        else:
            print("No Matches for \"%s\": " % lookingFor)

        if len(foundItems) != 0:
            for foundItem in foundItems:
                print(foundItem)
        openedFile.close()
        print("===============================================")


main()
