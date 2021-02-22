import os


def deleteUnneededFiles():
    for folderName, subFolderNames, filenames in os.walk(os.:
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


def main():
    deleteUnneededFiles


main()
