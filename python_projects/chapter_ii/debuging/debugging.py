import traceback
#raise Exception('This is the error')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '* (width-2))+symbol)
    print(symbol*width)
    
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: '+str(err))

try:
    raise Exception('This is a error message')
except:
    errorFile = open('B:\ATBSWP\python_projects\chapter_ii\debuging\\errorFile.txt', 'w')
    errorFile.write(traceback.format_exc()) #used to add error to a log file
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
