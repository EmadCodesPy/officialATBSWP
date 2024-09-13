def comma(param):
    for i in range(0,len(param)-1):
        print(str(param[i]), end=', ')
        pass
    print('and ' + str(param[-1]))

    
print()
spam = ['apples', 'bananas', 'pineapple', 12, 'kiosk']

comma(spam)