def printPicnic(itemDic, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemDic.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


def main():
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)


main()
