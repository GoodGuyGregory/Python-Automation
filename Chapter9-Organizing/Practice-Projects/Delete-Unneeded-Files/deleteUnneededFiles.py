import os


def deleteUnneededFiles(suppliedPath):
    # change directory
    os.chdir(suppliedPath)

    deletedFiles = []

    for folderName, subFolderNames, filenames in os.walk(os.getcwd()):
        print('The current folder is ' + folderName)

    # if there are iterables of multiple subfolders
        for subFolder in subFolderNames:
            print('Searching Subfolder of ' + folderName + ": " + subFolder)

            for filename in filenames:
                pathForFile = os.path.join(suppliedPath, folderName, filename)
                if os.path.getsize(pathForFile) > 100000000:
                    deletedFiles.append(filename)
                    print(filename + 'is larger than 100mb')

        #  if there are no folders in the directory
        for filename in filenames:
            pathForFile = os.path.join(suppliedPath, folderName, filename)
            if os.path.getsize(pathForFile) > 100000000:
                deletedFiles.append(filename)
                print(filename + 'is larger than 100mb')

        #  display findings
        print('===============================')
        print('found ' + str(len(deletedFiles)) + ' file(s)')
        print()
        response = input('Do you want to delete them? [Y/n] ')
        if response.lower() == 'y':
            for file in deletedFiles:
                print('deleting ' + file)
        else:
            print()
            print('keeping these files')
            print('exiting...')


def main():
    # directoryToSearch = input('enter a directory to search (pwd): ')

    directoryToSearch = '/Users/user/Desktop'

    deleteUnneededFiles(directoryToSearch)


main()
