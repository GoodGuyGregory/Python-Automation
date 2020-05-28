
def addToInventory(inventory, addedItems):
    print('adding loot to your inventory:')

    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            itemFound = addedItems[i]
            inventory[itemFound] = inventory[itemFound] + 1
            print(str(addedItems[i]) + ' added to inventory')
        elif addedItems[i] not in inventory:
            print('New item found!')
            # append new items with setDefault()
            newItem = addedItems[i]
            print(str(newItem))
            inventory[newItem] = 1


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
