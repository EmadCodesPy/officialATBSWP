import shutil, os

os.chdir('B:\\')
copyFile = shutil.copy('B:\ATBSWP\python_projects\\regex_search_file\\test2.txt', 'B:\ATBSWP\python_projects\chapter_ii\organizing_files')
#copies file from source and moves it to a specified directories
fileContent = shutil.copy('B:\ATBSWP\python_projects\\regex_search_file\\test.txt', 'B:\ATBSWP\python_projects\chapter_ii\organizing_files\\test1.txt')
#copies file conent to another directory under a different file name
copyTree = shutil.copytree('B:\ATBSWP\python_projects\own_work', 'B:\ATBSWP\python_projects\\own_work_backup')
#copies directory from source and all its conents to another directory

print(copyTree)