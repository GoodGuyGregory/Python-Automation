def pictureGrid(gridArg):
    # first row width
    for j in range(len(gridArg[0])):
        for i in range(len(gridArg)):
            print(gridArg[i][j], end=" ")
        print()


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.'], ]


def main():
    pictureGrid(grid)


main()
