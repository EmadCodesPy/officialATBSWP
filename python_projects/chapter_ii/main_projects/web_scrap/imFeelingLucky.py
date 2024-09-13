import requests, bs4, sys, webbrowser, re

print('Googling...')
search = ' '.join(sys.argv[1:])

res = requests.get('https://www.google.com/search?q=' + str(search))
res.raise_for_status()


soup = bs4.BeautifulSoup(res.text, features='lxml')
elems = soup.select('a')

#print(len(elems))

regex = re.compile(r'(https)(.*)')
repeated = re.compile(r'www\..*\.com')

allLinks = []
reapeatCheck = []
for link in elems:
    link = link['href']
    #print(link)
    mo = regex.search(str(link))
    if mo == None:
        pass
    else:
        allLinks.append(mo.group())

for item in allLinks:
    if repeated.search(item) in repeated.findall(allLinks):
        allLinks.remove(item)
 
for i in range(1,6):
    print(allLinks[i])
    webbrowser.open(allLinks[i])