import zipfile36 as zipfile, os

os.chdir('B:\\')

exampleZip = zipfile.ZipFile('cats.zip')
exampleZip.extractall('''you can specify a path here''') #Takes everything out of zip and into cwd
exampleZip.extract('spam.txt' ''',you can specify path after adding a comma''') #Extract single files
exampleZip.close()