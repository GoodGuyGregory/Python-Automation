def printTable(tableData):
    # creates an empty list for the widths for justificiation
    colWidths = [0] * len(tableData)
    largest = ''
    listCharFound = ''

# determine longest character in each nested list
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            # compare contents of the list at i
            listCharFound = tableData[i][j]
            print(listCharFound)
            if len(listCharFound) > len(largest):
                #  change the largest found
                largest = listCharFound
                # print(largest)
            #  set length for colWidths to that value
        colWidths[i] = len(largest)
        print(str(colWidths[i]))
        # clear the largest value
        largest = ''


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)


main()
