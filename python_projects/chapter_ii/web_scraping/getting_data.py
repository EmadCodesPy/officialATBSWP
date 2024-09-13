import bs4, os
os.chdir('B:\ATBSWP\python_projects\chapter_ii\web_scraping')

soup = bs4.BeautifulSoup(open('example.html'), features='lxml')

spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)