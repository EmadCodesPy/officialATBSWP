import shutil, os, re

regex = re.compile(r'''^(.*?)
                   ((0|1)?\d)-
                   ((0|1|2|3)?\d)-
                   ((19|20)\d\d)
                   (.*?)$
                   ''', re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = regex.search(amerFilename)
    
    if mo == None:
        continue
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    euroFilename = beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerPath = os.path.join(absWorkingDir, amerFilename)
    euroPath = os.path.join(absWorkingDir, euroFilename)
    
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerPath, euroPath)