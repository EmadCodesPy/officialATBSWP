tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob','Carol','David'],
             ['dogs','cats','moos','goose']]


def printTable(param):
    colWidths = [0] * len(param)
    for y in range(len(param)):
        for x in param[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)
    
    for x in range(len(param[0])):
        for y in range(len(param)):
            print(str(param[y][x]).rjust(colWidths[y]), end=' ')
        print()
        x += 1


printTable(tableData)

