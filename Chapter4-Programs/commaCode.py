import sys


# TEST ONE
def commaCode(listParam):

    if len(listParam) > 0:
        itemsToReturn = ''
        for i in range(len(listParam)):
            if i < len(listParam) - 1:
                itemsToReturn += (listParam[i] + ', ')
            else:
                itemsToReturn += ('and ' + listParam[i])

        return itemsToReturn
    elif not listParam:
        print('Please, enter some items to display... ')
        return 'exiting....'


def fillUserList():
    # declare empty list
    listFromUser = []
    while True:
        # grab a list of items
        inputStringToUse = str(input('enter an item for the list: '))
        if inputStringToUse != '':
            listFromUser.append(inputStringToUse)
            continue
        if inputStringToUse == '':
            print(commaCode(listFromUser))
            break


def main():

    # TEST ONE:
    # use a test list
    spam = ['apple', 'bananas', 'tofu', 'dogs']
    print(commaCode(spam))

    # TEST TWO:
    fillUserList()


    # commaCode(listToUse)
main()
