import os


def main():
    currentDirectory = os.getcwd()
    filesToSearch = os.listdir(currentDirectory)

    for filetoSearch in filesToSearch:
        print(filetoSearch)


main()
