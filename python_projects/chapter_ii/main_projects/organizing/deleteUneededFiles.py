import os


def deleteUndeededFiles(src, size):
    os.chdir(src)
    for foldername, subfolders, filenames in os.walk(src):
        for filename in filenames:
            if os.path.getsize(filename)/1000 > size:
                print('Removing %s from %s...' % (filename, foldername))
                #os.unlink(filename)


deleteUndeededFiles('B:\ATBSWP\selectiveCopyTest', 100)