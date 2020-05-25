def displayInventory(playerInventory):
    print('Inventory:')
    itemCount = 0
    for k, v in playerInventory.items():
        print(str(v) + ' ' + str(k))
        itemCount += v
    print('Total number of items: ' + str(itemCount))


def main():
    # inventory example:
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    displayInventory(stuff)


main()
