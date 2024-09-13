import os

pathExist = os.path.exists('/users/emad/desktop/python_projects')
#checks if a path exists (bool)
print(pathExist)
print()
isFile = os.path.isfile('/users/emad/desktop/download.jpeg')
#checks if item is a file (bool)
print(isFile)
print()
isDirectory = os.path.isdir('/users/emad/desktop')
#checks if item is a directory (bool)
print(isDirectory)
