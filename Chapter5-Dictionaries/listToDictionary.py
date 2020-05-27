
def addToInventory(inventory, addedItems):
    print('Adding Loot to Inventory:')

    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            itemFound = addedItems[i]
            inventory[itemFound] = inventory[itemFound] + 1
            print(str(addedItems[i]) + '')
        elif addedItems[i] not in inventory:

            # append with setDefault()


def displayInventory(playerInventory):
    print('Inventory:')
    itemCount = 0
    for k, v in playerInventory.items():
        print(str(v) + ' ' + str(k))
        itemCount += v
    print('Total number of items: ' + str(itemCount))


def main():
    # inventory example:
    inv = {'gold coin': 42, 'rope': 1}

    # example loot
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    addToInventory(inv, dragonLoot)
    displayInventory(inv)


main()
