import bs4, os

os.chdir('B:\ATBSWP\python_projects\chapter_ii\web_scraping')

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features='lxml')
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].get_text())
print(str(elems[0]))
print(elems[0].attrs)

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())
exampleFile.close()