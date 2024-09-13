import os, shutil

#os.unlink(path) #This deletes a file only
#os.rmdir(path) #This deletes a folder only if its empty of everything
#shutil.rmtree(path) #This deletes a folder and everything it contains




for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)
#This removes files endind in .rxt

for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)
#This is a safer practice beacuse it cant be undone once done