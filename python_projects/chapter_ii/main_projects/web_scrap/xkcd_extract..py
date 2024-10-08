import bs4, os, requests


url = 'https://xkcd.com'

os.chdir('B:\ATBSWP\python_projects\chapter_ii\main_projects\web_scrap')
os.makedirs('.\\XKCD', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find image.')
    else:
        comicUrl = 'https:'+comicElem[0].get('src')
        print('Downloading Image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('.\\XKCD', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')