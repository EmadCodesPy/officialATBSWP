import zipfile36 as zipfile, os

os.chdir('B:\\')
exampleZip = zipfile.ZipFile('cats.zip') #Opwns zipfile
nameList = exampleZip.namelist() #List of items in zip

zipInfo = exampleZip.getinfo('spam.txt') #gets info of a single file in a zip only
fileSize = zipInfo.file_size 

compressedSize = zipInfo.compress_size


print(nameList)
print(fileSize)
print(compressedSize)
print('')
print('Compressed size is %sx smaller than the original' %(round(fileSize/compressedSize, 2)))
exampleZip.close()