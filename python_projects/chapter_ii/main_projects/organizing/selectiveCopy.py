import os, shutil

'''Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from whatever
location they are in to a new folder.'''

def selectiveCopy(src, dst, end):
    for foldername, subfolders, filenames in os.walk(src):
        for filename in filenames:
            if filename.endswith(end):
                shutil.copy(os.path.join(foldername, filename), dst)
    print('Done')
    
selectiveCopy('B:\SCHOOL', 'B:\ATBSWP\selectiveCopyTest', 'txt')