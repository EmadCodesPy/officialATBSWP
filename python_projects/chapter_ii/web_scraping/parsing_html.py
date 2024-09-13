import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, features="lxml")
print(type(noStarchSoup))

exampleFile = requests.get('example.html')
exampleFile.raise_for_status()
exampleSoup = bs4.BeautifulSoup(exampleFile, features='lxml')
