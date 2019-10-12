# define print function
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


# first argument for the function
picnicItems = {'sandwiches': 4, 'apples': 3, 'cups': 2,
               'cookies': 6, 'Burritos': 3, 'sushi-rolls': 4}

printPicnic(picnicItems, 12, 5)
