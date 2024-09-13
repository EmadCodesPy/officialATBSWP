import requests, bs4

url = 'https://blog.fluidui.com/top-404-error-page-examples/'
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
elems = soup.select('a')
elems2 = []
for i in range(1, len(elems)):
    href = elems[i].get('href')
    try:
        start = href[:6]
    except:
        continue
    if start == 'https:':
        elems2.append(href)
    else:
        pass

for site in elems2:
    errorCheck = requests.get(site)
    try:
        errorCheck.raise_for_status()
    except Exception as err:
        print(str(err))