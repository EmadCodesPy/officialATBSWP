import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print(type(res))
#type is a response

print(res.status_code == requests.codes.ok)
#checks if request succeeded

print(res.text[:250])

res.raise_for_status() #checks for http error
playFile = open('B:\ATBSWP\python_projects\chapter_ii\web_scraping\\RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
#for loop adds content to the file

playFile.close()

