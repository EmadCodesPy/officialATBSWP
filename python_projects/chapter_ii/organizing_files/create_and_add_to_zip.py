import zipfile36 as zipfile, os

os.chdir('B:\\')
newZip = zipfile.ZipFile('newZip.zip', 'w') #Creates new zip in write mode
newZip.write('myexample.py', compress_type=zipfile.ZIP_DEFLATED) #Adds zip to file
newZip.close()

