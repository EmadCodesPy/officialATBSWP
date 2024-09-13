import os

fileSize = os.path.getsize('python_projects\Chapter_i\main_projects\pw.py')
#returns filesize in bytes
print(fileSize)

allDirectories = os.listdir('B:\\')
#returns all files in specified basename path
print(allDirectories)

totalSize = 0
for filename in allDirectories:
    totalSize += os.path.getsize(os.path.join('B:\\', filename))
print('Size of all files in desktop in is: ' + str(totalSize/1000000000) + ' GB')