def printTable(tableData):
    # creates an empty list for the widths for justificiation
    colWidths = [0] * len(tableData)
    largest = ''
    listCharFound = ''

# determine longest character in each nested list:
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            # compare contents of the list at i
            listCharFound = tableData[i][j]
            # print(listCharFound)
            if len(listCharFound) > len(largest):
                #  change the largest found
                largest = listCharFound
                # print(largest)
            #  set length for colWidths to that value
        colWidths[i] = len(largest)
        print(str(colWidths[i]))
        # clear the largest value
        largest = ''

    #  print elements with right justification:
    print(str(tableData[0][0]) + str(tableData[1][1]).rjust(colWidths[0]
                                                            ) + str(tableData[2][2].rjust(colWidths[0] + colWidths[1])))


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)
    # i = 0
    # while i < 3:
    #     if i == 0:
    #         for j in range(len(tableData[0])):
    #             print(tableData[0][j])
    #     i += 1


main()
