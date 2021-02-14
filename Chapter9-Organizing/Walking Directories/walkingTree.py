# an example of walking the directory tree
import os

for folderName, subFolderNames, filenames in os.walk(os.getcwd):
    print('The current folder is ' + folderName)

    # if there are iterables of multiple subfolders
    for subFolder in subFolderNames:
        print('Subfolder of ' + folderName + ": " + subFolder)

        for filename in filenames:
            print('file name ' + folderName + '')
