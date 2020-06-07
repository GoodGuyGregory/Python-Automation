def printTable(tableData):
    # creates an empty list for the widths for justificiation
    colWidths = [0] * len(tableData)

    # determine longest character in each nested list
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            # compare contents of the list at i
            largest = tableData[i][j]


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)


main()
