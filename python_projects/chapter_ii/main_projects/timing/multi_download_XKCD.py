import threading, requests, os, bs4

os.chdir('B:\ATBSWP\python_projects\chapter_ii\main_projects\\timing')
os.makedirs('.\\XKCD', exist_ok=True)

def downloadXKCD(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading the page https://xkcd.com/%s...' % urlNumber)
        res = requests.get('https://xkcd.com/%s' % urlNumber)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print("Could not find comic image.")
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()
            
            imageFile = open(os.path.join('.\\XKCD', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

downloadThreads = []
for i in range(1,50,9):
    downloadThread = threading.Thread(target=downloadXKCD, args=(i, i + 9))
    downloadThreads.append(downloadThread)
    downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done')
