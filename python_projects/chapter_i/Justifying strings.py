def printPicnic(dict, lwidth, rwidth):
    print('Picnic Items'.center(30, '='))
    for k,v in dict.items():
        print(str(k).ljust(lwidth, '.') + str(v).rjust(rwidth))


picnic = {'Apples': 15, 'Pie': 4, 'Sandwiches': 7}


printPicnic(picnic,15, 4) 