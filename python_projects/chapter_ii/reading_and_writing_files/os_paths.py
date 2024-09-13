import os

absolutePath = os.path.abspath('Python')

isItAbsolute = os.path.isabs(os.path.abspath('Python'))

findPath = os.path.relpath('main_projects', 'Users')

path = '/Users/Desktop/python_projects/chapter_i/main_projects'

print(absolutePath)
print(isItAbsolute)
print(findPath)
print(os.path.basename(path)+ '\t' + os.path.dirname(path))
print(os.path.split(path))