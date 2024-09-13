import os, shutil,re

regex = re.compile(r'(\D*)?(\d+)(\D*)?')



def fillingTheGaps(src):
    num = 1
    for file in os.listdir(src):
        a = regex.search(file)
        firstPart = a.group(1)
        endPart = a.group(3)
        newName = firstPart + str(num).zfill(3) + endPart
        shutil.move(os.path.join(src, file), os.path.join(src, newName))
        num += 1
    print('Done')
        
#fillingTheGaps('B:\ATBSWP\\newTest')

def addTheGap(src, gap):
    num = 1
    for file in os.listdir(src):
        a = regex.search(file)
        firstPart = a.group(1)
        numPart = a.group(2)
        endPart = a.group(3)
        if str(numPart) == str(gap).zfill(3):
                shutil.move(os.path.join(src, file), os.path.join(src, newName))
                num+=1
                continue
        newName = firstPart + str(num).zfill(3) + endPart
        shutil.move(os.path.join(src, file), os.path.join(src, newName))
        num += 1
    print('Done')

#addTheGap('B:\ATBSWP\\newTest', 2) 