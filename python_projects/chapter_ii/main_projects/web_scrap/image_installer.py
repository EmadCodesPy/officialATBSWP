import requests, bs4, os


os.chdir('B:\ATBSWP\python_projects\chapter_ii\main_projects\web_scrap')
os.makedirs('img_file', exist_ok=True)
res = requests.get('https://www.flickr.com/search/?text=cats')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')

elem = soup.select('.photo-list-photo-container img')

for i in range(1, len(elem)):
    try:
        img = requests.get('https:'+elem[i].get('src'))
        imgUrl = 'https:'+elem[i].get('src')
        img.raise_for_status()
        imageFile = open(os.path.join('.\\img_file', os.path.basename(imgUrl)), 'wb')
        print('Dowloading image %s...' %(os.path.basename(imgUrl)))
        for chunk in img.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except Exception as err:
        print('Error occurred: ' + str(err))


print('Done')