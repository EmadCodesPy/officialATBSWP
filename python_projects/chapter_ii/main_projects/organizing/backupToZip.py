import zipfile36 as zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    
    number = 1
    while True:
        zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFileName):
            break
        number = number+1
        
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')
        
    for foldername, subfolders, filenames, in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backupToZip('B:\\SCHOOL')
            