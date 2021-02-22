#! python3
# selectiveCopy - a program designed to allow for a specified selection file type
#  to be copied and added to a new folder

import os
import re


def selectivecopy():
    for folderName, subFolderNames, filenames in os.walk(os.getcwd()):
        print('The current folder is ' + folderName)

    # if there are iterables of multiple subfolders
        for subFolder in subFolderNames:
            print('SUBFOLDER OF ' + folderName + ": " + subFolder)

            for filename in filenames:
                print('FILE INSIDE ' + folderName + ': ' + filename)
                jpegRegex = re.compile(r'.jpg$')
                foundRegex = jpegRegex.search(filename)
                if foundRegex:
                    print("found %s" % filename)

        #  if there are no subfolders
        for filename in filenames:
            jpegRegex = re.compile(r'.jpg$')
            foundRegex = jpegRegex.search(filename)
            if foundRegex:
                print("FOUND FILE: %s" % filename)
        print('')


def main():

    selectivecopy()


main()
