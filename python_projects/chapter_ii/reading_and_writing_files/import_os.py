import os

allFiles = ['accounts.csv', 'essay.docx', 'passport.pdf']
for item in allFiles:
    path = os.path.join('user/bin/desktop', item)
    print(path)

currentDirectory = os.getcwd()
changeDirectory = os.chdir('/Users/Emad/Desktop/Python')

createDirectory = os.makedirs('/Users/Emad/Desktop/Temp_folder')

